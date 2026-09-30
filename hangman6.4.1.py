def check_valid_input(letter_guessed, old_letters_guessed):
#הפונקציה בודקת האם האות שניחשו היא תו אחד ובאנגלית, אם לא הפונקציה מחזירה FALSE אם כן הפונקציה מחזירה TRUE
#הפונקציה גם בודקת האם האות שניחשו נמצאת ברשימה של אותיות שכבר נוחשו אם כן מחזירה FALSE אם לא מחזירה TRUE
    letter_guessed=letter_guessed.lower()#הפכתי את האות שניחשו לאות קטנה

    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True



def main():
    #בדיקות בעזרת קריאות לפונקציה
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))#False
    print(check_valid_input('ep', old_letters))#False
    print(check_valid_input('$', old_letters))#False
    print(check_valid_input('s', old_letters))#True



if __name__ == '__main__':
    main()

