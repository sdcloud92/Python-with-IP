#Tuples
#A container to store different values, multiple pieces of information in a single variable similar to a list
#Defined with () instead of [] like Lists uses
#Tuples are immutable meaning they cannot be changed or modified unlike lists which is mutable,Lists are preferred
#Use cases for Tuples = numbers in your code that must not be changed

#LAB1 create first Tuple
tuple = ("Tesla", "Ferrari", "Lambourghini", "Aston Martin", "Porche")
print(tuple)

anime = ("Naruto", "Hunter x Hunter", "Sailor Moon", "Deathnote")
print(anime)

laptops = ("HP", "MacBook", "Samsung")
print(laptops)

korean_celebs = ("Choi Seo-eun", "Kim Go-eun", "Park Shin-hye")
print(korean_celebs)

europe = ("Spain", "Greece", "Romania", "Croatia", "Albania")
print(europe)

#LAB2 printing single value from tuple
tuple = ("Arsenal", "Manchester United", "Liverpool", "Chelsea", "West Ham", "Tottenham")
print(tuple[4])

anime = ("Naruto", "Hunter x Hunter", "Sailor Moon", "Deathnote")
print(anime[1])

laptops = ("HP", "MacBook", "Samsung")
print(laptops[2])

korean_celebs = ("Choi Seo-eun", "Kim Go-eun", "Park Shin-hye")
print(korean_celebs[0])

europe = ("Spain", "Greece", "Romania", "Croatia", "Albania")
print(europe[4])

#LAB3 example on why Tuples are immutable
caribbean = ("Jamaica", "Dominican Republic", "Puerto Rico", "Barbados", "Trinidad")
caribbean[3] = "Cuba"
print(caribbean[3]) #This will result in an error, you cannot make changes in Tuples

calisthenics = ("pull ups", "push ups", "sit ups", "squats", "sprints")
calisthenics[4] = "jumping jacks"
print(calisthenics[4]) #This will result in an error, you cannot make changes in Tuples

europe = ("Spain", "Greece", "Romania", "Croatia", "Albania")
europe[0] = "Portugal"
print(europe[0])

laptops = ("HP", "MacBook", "Samsung")
laptops[1] = "Dell"
print(laptops[1])

holidays = ("Christmas", "Easter", "Thanks giving")
holidays[2] = "420"
print(holidays[2])

#Lab4 Examples on why Lists are mutable i.e can be changed
caribbean = ("Jamaica", "Dominican Republic", "Puerto Rico", "Barbados", "Trinidad")
caribbean[3] = "Cuba"
print(caribbean[3]) #This will result in an error, you cannot make changes in Tuples

#Now will change () to [] to turn our tuple into a list which can be changed

caribbean = ["Jamaica", "Dominican Republic", "Puerto Rico", "Barbados", "Trinidad"]
caribbean[3] = "Cuba"
print(caribbean[3])
