def distance(num1, num2, num3):
    if abs(num1-num2)==1 or abs(num1-num3)==1:#אם אחד מהמספרים num2 או num3 "קרוב" ל-num1. "קרוב" = מרחק אבסולוטי 1.
        if (abs(num3-num1)>=2 and abs(num3-num2)>=2) or (abs(num2-num1)>=2 and abs(num2-num3)>=2):#אם אחד מהמספרים num2 או num3 "רחוק" משני המספרים האחרים. "רחוק" = מרחק אבסולוטי 2 ומעלה.
            return True
    return False

def main():
    #קריאות לפונקציה
    print(distance(1, 2, 10)) # True
    print(distance(4, 5, 3)) # False



if __name__ == "__main__":
    main()
