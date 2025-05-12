justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Number of members:", len(justice_league))
justice_league.extend(["Batgirl", "Nightwing"])
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
justice_league.remove("Green Lantern")
index_aquaman = justice_league.index("Aquaman")
index_flash = justice_league.index("Flash")
if index_aquaman < index_flash:
    justice_league.insert(index_flash, "Green Lantern")
else:
    justice_league.insert(index_aquaman, "Green Lantern")
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New Leader:", justice_league[0])