str=input("enter a string")
first_char =str[0]
new_string = str[1:].replace(first_char, 'e')
new_string = first_char + new_string
print(new_string)
#התכנית יוצרת מחרוזת חדשה שבה כל האותיות שהן אותו הדבר כמו האות הראשונה במחרוזת מוחלפות באות 'e'
