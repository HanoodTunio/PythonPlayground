import json


#read file
myJSON = open("F:\Python\quiz.json", "r")
jsonData = myJSON.read()

#parse
quiz = json.loads(jsonData)

list=quiz["questions"]
#print(list[0])

score=0

 
for x in range(len(list)):
    print("question" , x+1 ,": ", list[x].get("question"))
    jsonOption=list[x].get("options")
    for y in range(len(jsonOption)):
        print(y+1 ,jsonOption[y])
    correct=input("slect correct option: ")
    if(list[x].get("answer")==correct):
        score = score+1

print("Your final score is :", score , "/", len(list))       

