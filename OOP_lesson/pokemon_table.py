from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Eletric","Water","Fire"])

table.align = "l"
table.border = True
table.right_padding_width = 10


print(table)