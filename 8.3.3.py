def count_chars(my_str):
    # הסרת רווחים מהמחרוזת
    my_str = my_str.replace(" ", "")

    # יצירת מילון לספירת התווים
    my_dict = {}

    for char in my_str:
        if char in my_dict:
             #אם נתו כבר קיים נעלה את הvalue באחד
            my_dict[char] += 1
        else:
            #אם לא נוסיף אותו עם אחד בvalue
            my_dict[char] = 1

    return my_dict

def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

if __name__ == '__main__':
    main()

