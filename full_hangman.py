#משימה מתגלגת - איש תלוי
#הערה:הפורמט שבו הקוד קורא את הקובץ הוא כך שבקובץ על המילים בשורה ואחריהם פסיקים ללא רווחים יש בתיקייה קובץ הנקרא words העובד על פי פורמט זה וניתן להשתמש בו לביצוע הקוד
#שלב 1 - מסך פתיחה
def start_game(num):
    if num==1:
        HANGMAN_ASCII_ART="""  _    _                                         
        | |  | |                                        
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __ / |                      
                            |___/"""

        MAX_TRIES=6
        print("Welcome to the game Hangman")
        print(HANGMAN_ASCII_ART,"\n","you only have this amount of tries:",MAX_TRIES)
    else:
        print("game did not start")
        exit(1)#פקודה זו מפסיקה את הקוד לגמרי

def choose_word(file_path, index):

    with open(file_path, "r") as file:# קריאה מתוך הקובץ של המילים לבחירה
        content = file.read()

    # פיצול התוכן למילים לפי פסיקים
    words = content.split(",")

    # הסרת מילים שחוזרות על עצמן
    unique_words = set(words)
    unique_word_count = len(unique_words)

    # מיקום המילה שהתקבל כפרמטר (מיקומים מתחילים מ-1)
    num_words = len(words)
    if num_words == 0:
        return ("the file contains no words")

    # חשב את המיקום המעגלי
    circular_index = (index - 1) % num_words
    secret_word = words[circular_index]

    return unique_word_count, secret_word


# HANGMAN_PHOTOS. משתנה הוא מטיפוס מילון (dict)
# והוא מחזיק את שבעת המצבים של האיש התלוי .
HANGMAN_PHOTOS={"state0":"""                                           
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                                                  
            .G5!PY^                                            
            .PBP!                                          
            .G5.                                             
            .GY                                             
            .GY                                            
            .GY                                         
            .GY                                             
            .GY                                                       
            .GY                                                    
            .GY                                                   
            .GY                                           
            .GY                                       
            .GY                                                 
            .GY                                                         
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                          
""",
"state1":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                              ^^^:::^^:                   
            .GY                                                        
            .GY                                                          
            .GY                                                    
            .GY                                              
            .GY                                            
            .GY                                                   
            .GY                                                          
            .GY                                                        
            .GY                                                    
            .GY                                                 
            .GY                                               
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
""",
"state2":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                             .^^^:::^^:.                    
            .GY                                ..~.                        
            .GY                                  ~.                        
            .GY                                  ^                      
            .GY                                  ^                   
            .GY                                  ^               
            .GY                                  ^               
            .GY                                  ^                      
            .GY                                                        
            .GY                                               
            .GY                                       
            .GY                                             
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
""",
"state3":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                             .^^^:::^^:.                    
            .GY                                ..~.                        
            .GY                                  ~.                        
            .GY                                  ^::.                      
            .GY                                  ^. :::.                   
            .GY                                  ^.   .::.                 
            .GY                                  ^.                      
            .GY                                  ^:                        
            .GY                                                        
            .GY                                                   
            .GY                                                 
            .GY                                               
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
""",
"state4":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                             .^^^:::^^:.                    
            .GY                                ..~.                        
            .GY                                  ~.                        
            .GY                               .::^::.                      
            .GY                            .::.  ^. :::.                   
            .GY                           ::.    ^.   .::.                 
            .GY                                  ^.                      
            .GY                                  ^:                        
            .GY                                                        
            .GY                                                   
            .GY                                               
            .GY                                              
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
""",
"state5":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                             .^^^:::^^:.                    
            .GY                                ..~.                        
            .GY                                  ~.                        
            .GY                               .::^::.                      
            .GY                            .::.  ^. :::.                   
            .GY                           ::.    ^.   .::.                 
            .GY                                  ^.     .:                 
            .GY                                  ^:                        
            .GY                                 :~^.                       
            .GY                                     :^.                     
            .GY                                      .::                    
            .GY                                       .:.                    
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
""",
"state6":"""                                             
            ~YYYYYYYYYYYPPYYYYYYYYYYYYYYYYYYYY5Y~                         
            .GP:.......~5G7:...................:PP.                        
            .GY      .?GJ:                      YP.                        
            .GY     !P5^                        YP.                        
            .GY   ^5P!                          YP.                        
            .GY .JG?.                           YP.                        
            .G5!PY^                           ..Y5:..                      
            .PBP!                           :^^:...:^^:                    
            .G5.                           ~^        .~^                   
            .GY                           :~           !.                  
            .GY                           :!          .!.                  
            .GY                            ^~.       :~:                   
            .GY                             .^^^:::^^:.                    
            .GY                                ..~.                        
            .GY                                  ~.                        
            .GY                               .::^::.                      
            .GY                            .::.  ^. :::.                   
            .GY                           ::.    ^.   .::.                 
            .GY                                  ^.                      
            .GY                                  ^:                        
            .GY                                 :~^.                       
            .GY                               :^.  :^.                     
            .GY                             :^.     .::                    
            .GY                           .:.        .:.                    
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .GY                                                            
            .G5                                                            
!JJJJJJJJJ??YGGY?JJJJJJJJJ?^                                               
:~^^^^^^^^^~^::^^^^^^^^^^~^.                                                                                               
"""}

#הפונקציה מדפיסה את אחד משבעת המצבים של האיש התלוי, בעזרת:
#משתנה שנקרא num_of_tries שמייצג את מספר הניסיונות הכושלים של המשתמש עד כה.
#המשתנה HANGMAN_PHOTOS שהגדרתי.
def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS["state"+str(num_of_tries)]

def check_valid_input(letter_guessed, old_letters_guessed):
#פונקציית check_valid_input:
#בודקת אם התו הוא אות אנגלית אחת בלבד.
#אם כן, היא בודקת אם התו כבר נמצא ברשימה של התווים שניחשו.

    letter_guessed=letter_guessed.lower()#הפכתי את האות שניחשו לאות קטנה

    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed1, old_letters_guessed1):
#פונקציית try_update_letter_guessed:
#אם התו תקין ולא ניחשנו אותו קודם, הוא נוסף לרשימה ומוחזר True.
#אם התו לא תקין או כבר נמצא ברשימה, הפונקציה מדפיסה את ההודעה "X" ואת הרשימה הממוינת כשהתווים מופרדים ב-" <- " ומחזירה False.
    letter_guessed1=letter_guessed1.lower()#הפכתי את האות שניחשו לאות
    if(check_valid_input(letter_guessed1,old_letters_guessed1)):
        old_letters_guessed1.append(letter_guessed1)
        print(old_letters_guessed1)
        return True

    else:
        old_letters_guessed1.sort()
        str=" -> ".join(old_letters_guessed1[0:len(old_letters_guessed1):1])#חיבור התווים ברשימה המופרדים על ידי חץ
        print("X")
        print(str)
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    # יצירת מחרוזת עם קווים תחתונים עבור כל תו במילה הסודית
    len_word = ''

    for char in secret_word:
        # אם התו נמצא ברשימת התווים שנוחשו מוסיפים אותו למחרוזת ההתחלתית
        if char in old_letters_guessed:
            len_word += char + ' '
        else:
#אם לא אז מוסיפים קו תחתון
            len_word += '_ '

    return len_word.strip()

def check_win(secret_word, old_letters_guessed):
    count=0
    secret_word=secret_word.lower()#הפיכת המילה לאותיות קטנות
    for char in secret_word:#אם האות נמצאת הרשימת הניחושים הצובר עולה באחד
        if char in old_letters_guessed:
            count=count+1
    if count == len(secret_word):#אם הצובר שווה לאורך המילה הסודית זה אומר שהשחקן ניחש נכון את המילה
        return True#לכן נחזיר TRUE
    return False


def main():
    degel=True

    num=int(input("enter 1 if you wish to start the game"))
    print(start_game(num))

    file_path = input("Enter the path of the file: ")
    index = int(input("Enter the index of the word: "))

    result = choose_word(file_path, index)
    if result:#אם נכון הפונקציה החזירה משתנה מסוג טאפל
        unique_word_count, secret_word = result#נשווה את משתנים אלו לכל אחת מהמשתנים בטאפל
        #נדפיס את שני האיברים בטאפל בנפרד
        print("the amount of words that did not repeat themselfs:", unique_word_count)#כמה מילים לא חזרו על עצמן
        #print(secret_word)#את המילה הסודית שנבחרה לא נדפיס כי אנחנו לא רוצים לגלות מהי

    num_of_tries = 0
    old_letters = []
    counter=0
    print("let's start")
    print(print_hangman(counter))
    while degel:
        if num_of_tries<6:
        #בדיקות בעזרת קריאות לפונקציות
            letter_to_guess=input("enter a letter")
            print(try_update_letter_guessed(letter_to_guess, old_letters))#מחזיר TRUE אם האות לא נוחשה כבר
            print(show_hidden_word(secret_word, old_letters))
            if letter_to_guess not in secret_word:
                counter+=1
                print(print_hangman(counter))
            num_of_tries+=1

            if check_win(secret_word, old_letters) == True:
                degel=False
                print("you won :)")
        else:
            print("you lost :(")
            degel=False

if __name__ == '__main__':
    main()












