def process_input(file_name):

	incompatibilities = {}
	washing_times = {}

	with open(file_name) as file:
		for line in file:
			line = line.rstrip("\n")
			data = line.split()
			first_character = data[0]
			
			if first_character == 'c':
				continue

			elif first_character == 'e':
				if data[1] not in incompatibilities:
					incompatibilities[data[1]] = [data[2]]
				else:
					incompatibilities[data[1]].append(data[2])

			elif first_character == 'n':
				washing_times[ data[1] ] = data[2] 

	return incompatibilities, washing_times

incompatibilities, washing_times = process_input("data.txt")
