x = int(input("Тест на дебилизм. Введи число от 1 от 9. "))
while x <= 0 or x >= 10:
    x = int(input("Попробуй еще раз, я в тебя верю. "))
y = x*x
print("Ура! ты смог!  ", y)
input()
