const quotes = [
    { quote: "The world as we have created it is a process of our thinking.", author: "Albert Einstein" },
    { quote: "It is our choices that show what we truly are, far more than our abilities.", author: "J.K. Rowling" },
    { quote: "The only limit to our realization of tomorrow is our doubts of today.", author: "Franklin D. Roosevelt" },
    // Add more quotes dynamically here
];

const quoteList = document.querySelector('.quote-list');

quotes.forEach((quoteItem) => {
    const quoteElement = document.createElement('div');
    quoteElement.classList.add('quote-item');
    quoteElement.innerHTML = `
        <p class="quote-text">“${quoteItem.quote}”</p>
        <p class="author">— ${quoteItem.author}</p>
    `;
    quoteList.appendChild(quoteElement);
});
