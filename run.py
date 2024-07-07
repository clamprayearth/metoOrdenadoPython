import os
import platform

SO = platform.system()
#-------------COMANDO----------------------------------------------------------------------------------------------------------
if SO == 'Linux':                #Chamada do arquivo .py
    txt = "python3 arquiText.py"
else:            
    txt = "py arquiText.py"                                
os.system(txt)
#------------------------------------------------------------------------------------------------------------------------------

#-------------COMANDO----------------------------------------------------------------------------------------------------------
if SO == 'Linux':                #Comando para limpar a tela
    txt = "clear"
else:            
    txt = "cls"                                
os.system(txt)
#------------------------------------------------------------------------------------------------------------------------------

#-------------COMANDO----------------------------------------------------------------------------------------------------------
if SO == 'Linux':                #Chamada do arquivo .py
    txt = "python3 main.py < teste.txt"
else:            
    txt = "Sistema operacional não compativel com o arquivo run.py"                                
    print(txt)
os.system(txt)
#------------------------------------------------------------------------------------------------------------------------------
input ("Enter p/ continuar....") # <-------------------------------------------------------------------------------------------Parada de tela
#-------------COMANDO----------------------------------------------------------------------------------------------------------
if SO == 'Linux':                #Comando para testar o resultado com o algoritmo e o sort atraves do diff
    txt = "diff resultado.txt modelo.txt"                            
    output = os.system(txt)
    if output == 0:
        print("Sucesso........")
    else:
        print("Falha..........")
#------------------------------------------------------------------------------------------------------------------------------

#-------------COMANDO----------------------------------------------------------------------------------------------------------
if SO == 'Linux':                #Comando para apagar arquivo texto
    txt = "rm *.txt"
else:            
    txt = "del *.txt"                                
os.system(txt)
#------------------------------------------------------------------------------------------------------------------------------