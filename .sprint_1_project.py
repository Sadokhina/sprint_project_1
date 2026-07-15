print("Добрый день! Вас приветствует фитнес-бот")
#запрашиваем имя и ждем ответа
user_name = input("Как вас зовут? ") 
#запрашиваем возраст и ждем ответа
user_age = int(input("Сколько вам лет? "))
#запрашиваем рост и ждем ответа
user_height = input("Какой у вас рост  в метрах? ")
user_height_float = float(user_height)
#запрашиваем вес и ждем ответа
user_weight = input("Какой у вас вес в кг? ")
user_weight_float = float(user_weight)
#расчет индекса массы тела и округленное значения
bmi = user_weight_float / (user_height_float ** 2) 
bmi_round = round(bmi, 1)
#Рассчет нормы воды в миллилитрах, и далее перевод в литры:
water_ml = int(user_weight_float * 30)
water_l = water_ml / 1000
water_l_round = round(water_l, 1)
#расчет нормы воды в литрах округленного значения
print("-" * 40)
print("ОТЧЕТ по расчету ИМТ и нормы воды в день")
print("*" * 40)
print(f"Добрый день, {user_name}!, ({user_height} г.)")
print(f"Индекс массы тела (ИМТ) составил: {bmi_round}")
print(f"Норма воды: {water_l_round}, литров в день")
print("="*30)
print("Спасибо вам за уделенное время! Пейти воду с удовльствием и будете здоровы :)")