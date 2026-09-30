def format_list(my_list):
#הפונקציה מקבלת רשימת מחרוזות באורך זוגי. הפונקציה מחזירה מחרוזת המכילה את איברי הרשימה במיקומים הזוגיים, מופרדים בפסיק ורווח, ובנוסף גם את האיבר האחרון עם הכיתוב and לפניו.

    even_places= ", ".join(my_list[0:len(my_list):2])# חיבור עם פסיקים לתוך מחרוזת של כל המקומות הזוגיים
    last_place=", and " + my_list[-1]# הוספת המקום האחרון למחרוזת
    full= even_places + last_place#שרשור שתי המחרוזות יחדיו

    return full
def main():
    my_list=["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]#בדיקה
    print(format_list(my_list))#קריאה לפונקציה
if __name__ == '__main__':
    main()
