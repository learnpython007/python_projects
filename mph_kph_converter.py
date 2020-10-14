print("Converter - Miles to Kilometres ")
print("This app will convert minute miles to km or km to miles to help work out the speed you were running at. ") #This needs some rules adding in. 

def conversion_way(): #define which way the conversion will take place. 

    which_way = ''
    acceptable_answers = ['mile', 'km']

    while which_way not in acceptable_answers:
        which_way = input('What measurement do you have? (mile or km) ').lower()

    if which_way == 'mile':
        return ('mile', 'km')
    else:
        return ('km', 'mile')

def distance():

	while True:
		try:
			distance = float(input("Please input your distance. "))
		except:
			print("That was not an acceptable input. Please try again. ")
			continue
		else:
			print(f"The distance you have inputted is {distance}")
			break
	return distance

def dist_converter(distance, conversion): #convert the distance from miles to km or vice verca

	if conversion[0] == 'mile':
		unit = 1.60934
	else:
		unit = 0.621371

	convert = distance * unit

	print(f"You have run {convert} {conversion[1]}. ")

	return convert

def time(): #insert a function to turn time into a decimal number

	minutes = "Wrong"
	seconds = "Wrong"

	##### Change this to a try statement so it is open ended
	while True:
		try:
			minutes = int(input("How many minutes did your run take? "))
		except:
			print("That was wrong. ")
			continue
		else:
			break

	while seconds not in list(range(1, 60)):
		seconds = int(input("and how many seconds did your run take? "))

		decimal_seconds = ((100 / 60) * seconds) / 100

	return (minutes + decimal_seconds) / 60 #turns the inputted values into hour format for mph/kph

def speed_of_run(distance, time):

	speed = distance / time

	return speed


units = conversion_way()
run_dist = distance()
run_time = float(time())
dist_convert = dist_converter(run_dist, units)
run_speed = speed_of_run(dist_convert, run_time)

print(f"It took you {run_time:.2f} hours to run {dist_convert:.2f} {units[1]}. The average speed of your run was {run_speed:.2f}{units[1]}/h. ")
