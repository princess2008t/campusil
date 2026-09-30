def copy_file_content(source, destination):
    # קריאה מקובץ מקור וכתיבה לקובץ יעד
    with open(source, "r") as input_file:
        content = input_file.read()  # קריאה של כל התוכן מהקובץ המקורי

    with open(destination, "w") as output_file:
        output_file.write(content)  # כתיבה של התוכן לקובץ היעד
        

def main():
    source=input("enter file path")
    destination=input("enter filr path")
    copy_file_content(source, destination)
if __name__ == '__main__':
    main()
