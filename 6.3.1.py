#הפונקציה מקבלת שתי רשימות המכילות איברים מהטיפוסים int ו-float בלבד. הפונקציה מחזירה אמת אם שתי הרשימות מכילות בדיוק את אותם האיברים (גם אם בסדר שונה), אחרת, הפונקציה מחזירה שקר.
def are_lists_equal(list1, list2):
    #נניח שהקלטים תקינים
    list1.sort()#נציין את שתי הרשימות כך שיהיו בסדר עולה
    list2.sort()
    if list1[0:len(list1):1] == list2[0:len(list2):1]:#נבדוק אם שוות מתחילתם ועד סופם
        return True
    return False

def main():
    list1 = [0.6, 1, 2, 3]#בדיקה
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

if __name__ == '__main__':
    main()
