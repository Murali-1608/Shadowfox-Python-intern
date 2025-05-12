total_jacks = 100
done_jacks = 0
set_size = 10

while done_jacks < total_jacks:
    print(f"Do 10 jumping jacks.")
    done_jacks += set_size

    if done_jacks >= total_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {done_jacks} jumping jacks.")
            break
        else:
            remaining = total_jacks - done_jacks
            print(f"{remaining} jumping jacks remaining.")
    elif tired in ["no", "n"]:
        remaining = total_jacks - done_jacks
        print(f"{remaining} jumping jacks remaining.")
    else:
        print("Invalid input. Continuing workout...")