from inputProcessor import process_input


INCOMPATIBILITIES, WASHING_TIMES = process_input("data.txt")


def main():
	
	oredered_washing_times = dict(sorted(WASHING_TIMES.items(), key=lambda item: int(item[1]), reverse=True))

	wash_number = 1
	washing_time = 0
	enqueed_clothing= set()
	washes = []

	with open("output.txt", 'w') as output:

		for actual_clothing in oredered_washing_times.keys():

			if actual_clothing in enqueed_clothing:
				continue

			wash = {actual_clothing}
			output.write(actual_clothing + " " + str(wash_number) + "\n")
			washing_time += int(oredered_washing_times[actual_clothing])
			enqueed_clothing.add(actual_clothing)	

			for clothing in oredered_washing_times.keys():
				if is_incompatible(clothing, wash) or clothing in enqueed_clothing:
					continue

				wash.add(clothing)
				output.write(clothing + " " + str(wash_number) + "\n")
				enqueed_clothing.add(clothing)

			wash_number += 1
			washes.append(wash)

		print(washing_time)
		print(washes)	


def is_incompatible(cloth1, wash):
	for clothing in wash:
		if cloth1 in INCOMPATIBILITIES[clothing]:
			return True
	return False


main()
