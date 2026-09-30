def numbers_letters_count(my_str):
    #הפונקציה מקבלת מחרווזת ויוצרת רשימה על פי מספר המספרים שיש במחרוזת ומספר התווים שאינם מספרים שיש במחרוזת
    numbers=["0","1","2","3","4","5","6","7","8","9"]#רשימה של המספרים
    count=0
    for i in range (len(my_str)):
        if my_str[i] in numbers[0:len(numbers):1]:
            count=count+1#עולה באחד כל פעם שמופיע מספר
    new_list=[]
    tav=len(my_str) - count
    new_list.append(count)
    new_list.append(tav)
    return new_list

def main():
    print(numbers_letters_count("Python 3.6.3"))#בדיקה

if __name__ == '__main__':
    main()
