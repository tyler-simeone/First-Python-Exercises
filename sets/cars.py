#### Sets Practice ####

showroom = set()

showroom.update(["Ferrari 458 Speciale", "Ferrari F12 TDF", "Porsche GT3 RS", "Rivian R1T"])

print(len(showroom))

showroom.add("Ferrari 458 Speciale")

showroom.update(["Tesla Model S p100D", "1969 Chevy Camaro"])

showroom.discard("Tesla Model S p100D")

print(showroom)

junkyard = {"Old piece of crap", "1999 Buick LaSomething", "2000 Lincoln Navigator", "1969 Chevy Camaro"}

# shows which car in junkyard set is also in showroom set
print(junkyard.intersection(showroom))
# shows showroom set combined with union set
print(junkyard.union(showroom))