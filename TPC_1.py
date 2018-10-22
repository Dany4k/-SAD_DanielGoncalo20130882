st = "[1,2,3,1]"
if(st[0] == "{" and st[-1] == "}"):
	print("1") 
else: 
	print("0")
	
if(st[0] == "[" and st[-1] == "]"):
	print("1") 
else: 
	print("0")
	
if(st[0] == "(" and st[-1] == ")"):
	print("1") 
else: 
	print("0")
	
#Aqui verifica apenas o primeiro char. Um array nunca pode começar com parentesis abertos.	
if(st[0] == ")"):
	print("0")
	
if(st[0] == "]"):
	print("0")

if(st[0] == "}"):
	print("0") 

#Para verificar que está correcto basta verificar que existe um "1" no output final. Caso o output seja apenas composto por "0" alguma das condições
#não é cumprida!