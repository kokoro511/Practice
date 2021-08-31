from prac6.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()