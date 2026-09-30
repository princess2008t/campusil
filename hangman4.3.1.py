tav=input("enter a letter")#קלט

if len(tav)>1 and tav.isalpha():#האם אורך הצחרוזת גדולה מ1 והיא רק אותיות
    print("E1")

if not tav.isalpha() and len(tav)==1:#האם התו הוא לא אות באנגלית
    print("E2")

if len(tav)>1 and not tav.isalpha(): #האם אורך המחרוזת גדולה מאחד וגם לא כל התווים אותיות באנגלית
    print("E3")

if tav.isalpha() and len(tav)==1:
    print(tav.lower())

