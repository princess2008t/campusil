temp_str=input("enter the temp in f or c")#קלט מהמשתמש
if "c" in temp_str:
    temp=temp_str.replace("c", "")#מחיקת האות על מנת להמיר למספר עשרוני
    print((9 * float(temp) + (32*5))/5,"f")#חישוב על מנת להמיר

elif "C" in temp_str:
    temp=temp_str.replace("C", "")
    print((9 * float(temp) + (32*5))/5,"F")


elif "f" in temp_str:
    temp=temp_str.replace("f", "")
    print(((5 * float(temp)) - 160)/9,"c")

elif "F" in temp_str:
    temp=temp_str.replace("F", "")
    print(((5 * float(temp)) - 160)/9,"C")

else:
    print("you didn't add the type of the temp, try again")
