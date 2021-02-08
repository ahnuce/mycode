movies = {

"scifi":{"best":"matrix", "worst":"matrix reloaded"},
"comedy":{"best":"spaceballs","worst":"click"},
"horror":{"best":"conjuring","worst":"glass house"}

}


#print("Choose a genre: scifi, comedy, or horror")
#genre= input(">")

#print("Do you want the best or the worst?")
#choice= input(">")

#this is the best/worst genre: answer
#print("This is the " + choice + "of" + genre + ":" + movies[genre][choice])
# concatenation is the joining together of strings (ONLY STRINGS) into one big sttring!

#F STRING
#print(f"This is the {choice} of {genre}: {movies[genre][choice]}")

movies= [{"scifi":{"best":"matrix","worst":"matrix reloaded"}},{"comedy":{"best":"spaceballs","worst":"click"}},{"horror":{"best":"conjuring","worst":"glass house"}},]
#1. prompt user for scifi, comedy or horror
print("Access  a genre: scifi, comedy, or horror")


genre = input(">")
choice = input(">")

#if input = false:
 #   print("you messed this up")
  #  quit()
print(f"The {choice} of {genre}  film is: {my.Test[genre][choice]}")
