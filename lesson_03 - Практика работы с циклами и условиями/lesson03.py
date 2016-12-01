#Практика работы с циклами и условиями

residence_limit = 90  # 45, 60
schengen_constraint = 180
visits = [[1, 10], [16, 45], [91, 180], [181, 181]]
#Проверка на корректное заполнение списка дат въездов и выездов в ЕС
#--------------------------------------------------------------------
for visit in visits:
	if not isinstance(visit, list):
		raise Exception("Ошибка в построении списка дат", visit)

#Проверка дат въездов и выездов на последовательность
#---------------------------------------------------------------------
for number_visit in range(len(visits) - 1):
	for number_next_visit in range(number_visit + 1, len(visits)):
		if visits[number_visit][1] > visits[number_next_visit][0]:
			raise Exception("Ошибка: наложение поездок", number_next_visit)

for visit in visits:
	if visit[0] > visit[1]:
		raise Exception("Ошибка: дата въезда позже даты выезда", visit)
		
#Проверка дат въездов и выездов на residence_limit
#---------------------------------------------------------------------
one_visit = 0
for visit in visits:
	one_visit = visit[1] - visit[0] + 1
	if one_visit > residence_limit:
		raise Exception("Согласно срокам действия Вашей визы, Вы можете пребывать в ЕС не болле " + str(residence_limit) + " дней, измените даты Вашей поездки", visit)

#решение
#---------------------------------------------------------------------
x = 0 #используется во фразе: "Выше представлены сроки поездок, Вашего тура №"
exit = 0 #переменная exit используется для обозначения плавающего начала и конца срока schengen_constraint

for visit in visits:
	while True:
		x += 1
		tour = 0 #одна поездка - разность м/у датой въезда и выезда
		exit_date = [] #список дат выезда
		sum_tour = [] #список всех поездок, которые входят в коридор(180 дней) и в сумме не более 90 дней
		if exit == len(visits):
			break

		for visit in visits:	
			if visits[exit][0] <= visit[1] < visits[exit][0] + schengen_constraint: #опр. даты всех выездов, кот. входят в коридор(180 дней)
				tour += visit[1] - visit[0] + 1 #суммы всех поездок, кот. входят в коридор(180 дней)
				if tour <= residence_limit:  #если поездки в сумме не более 90 дней, то...
					exit_date.append(visit[1]) #добавить в список дат выездов очередную дату выезда
					sum_tour.append(tour) #добавить в список поездок, которые удовлетворяют всем условиям, очередную поездку
					print(visit) #вывести на печать поездки, которые удовлетворяют всем условиям
					
					new_trip = residence_limit - sum_tour[-1] #остаток дней для новой поездки
					corridor_rest = visits[exit][0] + schengen_constraint - max(exit_date) - 1 #остаток коридора дней для новой поездки
		
		if sum_tour[-1]:
			print("Выше представлены сроки поездок, Вашего тура №" + str(x) + ":")
			print("Количество дней в сумме: %0.f" %sum_tour[-1])
			
			print("\nСогласно срокам пребывания и установленному коридору, на новую поездку у Вас еще остается " + str(new_trip) + " дней.")
			if new_trip:
				print("\nЕе Вы можете совершить в течение остатка коридора из " + str(corridor_rest) + " дней.")
			
			if corridor_rest == 0 or not new_trip:
				print("\nт.е. Вы не можете совершить больше ни одной поездки.")
			elif corridor_rest < new_trip:
				print("\nт.е. Вы можете совершить поездку только на протяжении %.0f дней." % corridor_rest)
				
		exit = exit + len(exit_date)		
		print("\n***-***-***\n")