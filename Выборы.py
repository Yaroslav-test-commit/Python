age = int(input("Введите Ваш возраст: "))
citizenship = input("Вы являетесь гражданином страны? (да/нет): ").strip().lower() == "да"
disqualified = input("Вы привлекались к уголовной/административной ответственности? (да/нет): ").strip().lower() == "да"
if age >= 18 and citizenship and not disqualified:
    print("Вы имеете право принять участие в голосовании")
else:
    print("Вы пока не можете принять участие в голосовании")
