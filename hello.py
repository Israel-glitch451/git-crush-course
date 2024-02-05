names = ["Elton", "Godsway", "Peter", "Fred"]
guess = True
while guess:
    for name in names:
        if name == "Godsway":
            guess = False
            print(f"Hello {name}")
        else:
            print(f"Not needed here")