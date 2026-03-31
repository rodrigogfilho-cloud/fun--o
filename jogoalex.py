import funcao
from playsound import playsound 

print("VAMOS COMEÇAR NOSSO JOGO... UHAHAHAHAHAHAHAHAHAHA")
playsound("risada_malvada.mp3")
playsound("intro_game.mp3")

resposta = int(input("Quanto é 2 + 2: "))
def mostrar_sixseven():
    print("""

   __      _____  
U /"/_ u  |___ "| 
\| '_ \/     / /  
 | (_) |  u// /\  
  \___/    /_/ U  
 _// \\_  <<>>_   
(__) (__)(__)__)  
 
""")
    playsound("sixsevenkid.mp3")

def mostrar_derrota():
    print("Você é um ENERGÚMENO")
    playsound("gameover.mp3")

if resposta == 4:
    funcao.mostrar_vitoria()
elif resposta == 67:
    mostrar_sixseven()
else:
    mostrar_derrota()

