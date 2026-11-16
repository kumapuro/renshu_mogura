def start button on click(event):
    document.getElementById("start button").disabled=True
    game["turns"]=GAME TURNS
    game["score"]=0
    next turn()

def canvas on click(event):
    rect=canvas.getBoundingClientRect()
    click x = event.clientX - rect.left
    click y = event.clientY - rect.top
    
    if not game["hide"]:
        
        if(game["mx"] <= click x <= game["mx"]+WIDTH and
           game["my"] <= click y <= game["my"]+WIDTH):
           game["score"]+=1
           game["hide"]=True