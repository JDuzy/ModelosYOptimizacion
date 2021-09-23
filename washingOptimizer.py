from inputProcessor import process_input


INCOMPATIBILITIES, WASHING_TIMES = process_input("data.txt")


def main():
	
	oredered_washing_times = dict(sorted(WASHING_TIMES.items(), key=lambda item: int(item[1]), reverse=True))

	wash_number = 1
	washing_time = 0
	enqueed_clothing= set()
	#washes = []

	with open("output.txt", 'w') as output:

		for actual_clothing in oredered_washing_times.keys():

			if actual_clothing in enqueed_clothing:
				continue

			#wash = [actual_clothing]
			output.write(actual_clothing + " " + str(wash_number) + "\n")
			#washing_time += int(oredered_washing_times[actual_clothing])
			enqueed_clothing.add(actual_clothing)	

			for clothing in oredered_washing_times.keys():
				if is_incompatible(actual_clothing, clothing) or clothing in enqueed_clothing:
					continue

				#wash.append(clothing)
				output.write(clothing + " " + str(wash_number) + "\n")
				enqueed_clothing.add(clothing)

			wash_number += 1
			#washes.append(wash)


def is_incompatible(cloth1, cloth2):
	return cloth2 in INCOMPATIBILITIES[cloth1]


main()
