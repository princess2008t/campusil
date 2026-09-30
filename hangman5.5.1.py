def is_valid_input(letter_guessed):
    #הפונקציה בודקת אם התו שניחשו אכן תקין כלומר תו אחד שהוא באנגלית

    if len(letter_guessed)>1 and letter_guessed.isalpha():#האם אורך הצחרוזת גדולה מ1 והיא רק אותיות
        return False

    if not letter_guessed.isalpha() and len(letter_guessed)==1:#האם התו הוא לא אות באנגלית
        return False

    if len(letter_guessed)>1 and not letter_guessed.isalpha(): #האם אורך המחרוזת גדולה מאחד וגם לא כל התווים אותיות באנגלית
        return False

    if letter_guessed.isalpha() and len(letter_guessed)==1:#מחזיר אמת אם האות שניחשו היא בעלת תו אחד והיא אות באנגלית
        return True


def main():
    #בדיקות בעזרת קריאות לפונקציה
    print(is_valid_input('a'))  # True
    print(is_valid_input('A'))  # True
    print(is_valid_input('$'))  # False
    print(is_valid_input("ab"))  # False
    print(is_valid_input("app$"))  # False


if __name__ == '__main__':
    main()
