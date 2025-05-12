const words = [
  { word: "javascript", hint: "Popular scripting language for web development" },
  { word: "hangman", hint: "A classic word guessing game" },
  { word: "frontend", hint: "What users see in a website" },
  { word: "keyboard", hint: "Used for typing" },
  { word: "python", hint: "A programming language named after a comedy group" },
  { word: "fortran", hint: "oldest programming language"},
  { word: "hyper text markup language", hint: "HTML abbreviation"}
];

let selectedWord, hint, attempts, guessedLetters;

function initializeGame() {
  const random = words[Math.floor(Math.random() * words.length)];
  selectedWord = random.word.toLowerCase();
  hint = random.hint;
  attempts = 6;
  guessedLetters = [];

  document.getElementById("hint").textContent = `Hint: ${hint}`;
  document.getElementById("attempts").textContent = attempts;
  document.getElementById("message").textContent = "";
  generateWordDisplay();
  generateKeyboard();
}

function generateWordDisplay() {
  const display = selectedWord.split("").map(letter =>
    guessedLetters.includes(letter) ? letter : "_"
  ).join(" ");
  document.getElementById("word-display").textContent = display;

  if (!display.includes("_")) {
    document.getElementById("message").textContent = "🎉 You Won!";
    disableAllButtons();
  }
}

function generateKeyboard() {
  const keyboard = document.getElementById("keyboard");
  keyboard.innerHTML = "";

  for (let i = 97; i <= 122; i++) {
    const letter = String.fromCharCode(i);
    const button = document.createElement("button");
    button.textContent = letter;
    button.onclick = () => handleGuess(letter, button);
    keyboard.appendChild(button);
  }
}

function handleGuess(letter, button) {
  button.disabled = true;
  if (selectedWord.includes(letter)) {
    guessedLetters.push(letter);
    generateWordDisplay();
  } else {
    attempts--;
    document.getElementById("attempts").textContent = attempts;
    if (attempts === 0) {
      document.getElementById("message").textContent = ` Game Over! The word was "${selectedWord}".`;
      disableAllButtons();
    }
  }
}

function disableAllButtons() {
  const buttons = document.querySelectorAll("#keyboard button");
  buttons.forEach(button => button.disabled = true);
}

// Initialize the game on page load
window.onload = initializeGame;
