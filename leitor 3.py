arq = open('multp/multp_2_49.dat', 'r') 
texto = arq.readlines() 
lines = [t.strip().split() for t in texto]
polinomioA = []
polinomioB = []
grau = int(lines[0][0])

for linha in lines[1:]:
	if polinomioA == []:
		polinomioA.append(linha)
	else: 
		if linha != []:
			polinomioB.append(linha)
	
	
print("A", polinomioA)
print("B", polinomioB)
print("Grau", grau) 
arq.close()
