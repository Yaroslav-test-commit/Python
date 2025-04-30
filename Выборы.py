age = int(input())
citizenship = input("Вы являетесь гражданином страны? (да/нет): ").strip().lower() == "да"
disqualified = input("Вы были дисквалифицированы? (да/нет): ").strip().lower() == "да"
admission = "Вы имеете право принять участие в голосовании" if age >= 18 and citizenship and not disqualified else "Вы пока не можете принять участие в голосовании"

print(admission)
