days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days)
print(type(days))
print("Mon" in days)  # common operator
print(days[3])
print(len(days))
print(days)
days.append("Sat")  # mutable operation
print(days)
days.insert(4, "Sun")
print(days)
days.reverse()
print(days)

# for a list it can use both common and mutable operation
# but tuples can only operate common operation
sport = ("a", "b", "C", "D", "E")  # tuple
print(sport)
print(type(sport))
# dictionary
Abhiru = {
    "name": "Abhiru",
    "Age": 23,
    "SriLankan": True,
    "Single": False,
    "Profession": "Data analytics",
    "fav_food": ["Submarine", "Chocolate"]
}
print(Abhiru)
Abhiru["handsome"] = True
print(Abhiru)
