import random
from js import setTimeout, document

GAME TURNS = 30
INTERVAL = 1000
WIDTH =50

info = document.getElementById("info")
canvas=document.getElementById("canvas")
context=canvas.getContext("2d")

game={
    "turns":GAME TURNS, #残りのゲームターン数
    "score":0,#スコア
    "mx":0, #モグラｘ座標
    "my":0, #モグラｙ座標
    "hide":True, #モグラが隠れているかどうか
}

def next turn():
    if game["turns"]<=0:
        game over()
        return
    game["turns"]-= 1 #残りターン数を１減らす
    update mogura() 
    update screen()
    setTimeout(next turn, INTERVAL)

def update mogura():
    game["hide"]=not game["hide"]
    if not game["hide"]:
        game["mx"]=random.randint(0,canvas.width-WIDTH)
        game["my"]=random.randint(0,canvas.height-WIDTH)

def update screen():
    context.clearRect(0,0,canvas.width, canvas.height)
    if not game["hide"]:
        context.fillstyle="brown"
        context.fillRect(game["mx"],game["my"],WIDTH,WIDTH)
    info,innerText=(f"スコア:{game['score']}点/"
                    f"残り時間:{game['turns']}")

def game over():
    info.innerText=f"モグラ叩き終了:スコア{game['score']}点"
    document.getElementById("start button").disabled=False