## Application interface for auto-generating MySQL schema 



next_field = True

fields = []

print("Welcome to MySQL Cheat Buddy!\n")


tab_name = input("Begin by adding a table name: ")


print("\nTable {0} created\n".format(tab_name))




print("Please add a field and press enter after each field, followed by table options.\n\nIf you are done adding fields, enter \"_done\", and the prompt will continue\n\n")
print("The program does not add table options automatically, you must enter those along with your field name,\nlike you normally would when creating a table.\n")


while(next_field):

	field = input("Enter field name and options: ")

	if field.lower() == "_done":
		next_field = False
	else:
		fields.append(field)



print(fields)