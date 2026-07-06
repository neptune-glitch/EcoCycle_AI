from skills.identify import identify
from skills.retrieve import retrieve
from skills.advise import advise

item = identify("images/bottle.jpg")

knowledge = retrieve(item)

answer = advise(item, knowledge)

print(answer)