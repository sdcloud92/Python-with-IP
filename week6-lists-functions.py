#LAB 1 - Extend Function
#Combines lists together in the output

anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
cars = ["Tesla", "BMW", "Range Rover", "Aston Martin", "Mercedes"]

anime.extend(cars) 
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]

korean_dramas.extend(dc_characters) 
print(korean_dramas)

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]

languages.extend(dc_villains) 
print(languages)

konoha = ["Hidden Leaf Village", "Hidden Sand Village", "Hidden Mist Village", "Hidden Cloud Village", "Hidden Stone Village"]
hokage = ["Hashirama", "Tobirama ", "Minato", "Tsunade", "Kakashi"]

konoha.extend(hokage) 
print(konoha)

asia = ["South Korea", "Japan", "Phillipines", "Thailand"]
south_america = ["Colombia", "Brazil", "Venezuela"]

asia.extend(south_america) 
print(asia)

#LAB 2 - Append Function
#Add an element to the end of a list

anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.append("Death Note") 
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.append("Penthouse")
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.append("Nightwing")
print(dc_characters)

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
languages.append("Arabic")
print(languages)

dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]
dc_villains.append("Two-Face")
print(dc_villains)


#LAB 3 - Insert Function
#Insert an element in the list in place of the previous element but keeps previous element
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.insert(0, "Shaman King") 
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.insert(1, "Penthouse")
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.insert(3,"Nightwing")
print(dc_characters)

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
languages.insert(4, "Arabic")
print(languages)

dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]
dc_villains.insert(5, "Two-Face")
print(dc_villains)


#LAB 4 - Remove Function
#Remove any element in a list
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.remove("Naruto") 
print(anime)

anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.remove("Bleach") 
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.remove("Crash Landing On You")
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.remove("Aquaman")
print(dc_characters)

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
languages.remove("Chinese")
print(languages)

dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]
dc_villains.remove("Harley Quinn")
print(dc_villains)

#LAB 5 - Clear Function
#Clears list
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.clear() 
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.clear()
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.clear()
print(dc_characters)

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
languages.clear()
print(languages)

dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]
dc_villains.clear()
print(dc_villains)

#LAB 6 - Index Function
#To see if a certain element/value exists within the list, and what number in the list?
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
print(anime.index("Attack on Titan"))

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
print(korean_dramas.index("Itaewon Class"))

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
print(dc_characters.index("Batman"))

languages = ["Chinese", "Korean", "Japanese", "Spanish", "Portuguese"]
print(languages.index("Korean"))

dc_villains = ["Joker", "Lex Luther", "Harley Quinn", "The Penguin", "The Riddler"]
print(dc_villains.index("The Penguin"))


#LAB 7 - Count Function
#Counts how many times a value appears in the list
anime = ["Naruto", "Bleach", "Bleach", "Bleach", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
print(anime.count("Bleach"))

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
print(korean_dramas.count("Itaewon Class"))

dc_characters = ["Batman", "Superman", "Batman", "The Flash", "Batman", "Aquaman", "Batman", "Wonderwoman", "Batman"]
print(dc_characters.count("Batman"))

languages = ["Chinese", "Korean", "Chinese", "Japanese", "Chinese", "Spanish", "Portuguese"]
print(languages.count("Korean"))

dc_villains = ["Joker", "Lex Luther", "Joker", "The Penguin", "The Riddler"]
print(dc_villains.count("The Penguin"))


#LAB 8 - Sort Function
#Sorts your list in alphabetical or ascending order
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.sort()
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.sort()
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.sort
print(dc_characters)

languages = ["Chinese", "Japanese", "Spanish", "Portuguese"]
languages.sort
print(languages)

dc_villains = ["Joker", "Lex Luther", "The Penguin", "The Riddler"]
dc_villains.sort()
print(dc_villains)


#LAB 9 - Reverse Function
#Outputs list in reverse order
anime = ["Naruto", "Bleach", "Attack on Titan", "Captain Tsubasa", "Dragonball Z"]
anime.reverse()
print(anime)

korean_dramas = ["Itaewon Class", "Crash Landing On You", "My Name", "Singles Inferno", "Start Up"]
korean_dramas.reverse()
print(korean_dramas)

dc_characters = ["Batman", "Superman", "The Flash", "Aquaman", "Wonderwoman"]
dc_characters.reverse()
print(dc_characters)

languages = ["Chinese", "Japanese", "Spanish", "Portuguese"]
languages.reverse()
print(languages)

dc_villains = ["Joker", "Lex Luther", "The Penguin", "The Riddler"]
dc_villains.reverse()
print(dc_villains)