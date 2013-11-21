# Méthodes de tris via une Liste, pour augmenter les performances, supprimer les prints
# liste = [15, 25, 65, 98, 656, 23, 4564, 8979, 156, 999999, 1231, 5645, 89789, 123123, 0, 0 ,0 ,0 ,5 ,232 ,1, 54665, 45 ,7 ,89, 78]
def tri(liste):
	iT = time.time()
	x = 0
	y = 0
	while(x < len(liste) - 1): # Si pour une valeur de x, le terme de rang x est inférieur à celui de x + 1 , alors on sort de la boucle while.
		if(liste[x] > liste[x + 1]): # Si un terme est supérieur au suivant, on le range apres et on repart du début...
			liste.insert(x + 2, liste[x])
			liste.remove(liste[x])
			x = 0
		elif(liste[x] < liste[x + 1]): # Si un terme est inférieur au suivant, on continue le tri... 
			x += 1
		else: # Si un terme est égal au suivant
			x += 1
	fT = time.time()
	t = fT - iT
	print("Temps total de tri: " + str(t) + " secondes")

	
#Créer une table de multiplication, de x à y (exemple, table de 2 sur 10 termes)
def table(nb, max):
	x = 0
	while(x < max):
		x += 1
		result = nb * x
		print(str(nb) + " fois " + str(x) + " = " + str(result))

def etoile(nbEtoile):
	x = 0
	etoile = "*"
	while(x <= nbEtoile):
		print(etoile)
		x += 1
		etoile += "*"

#Créer une suite géométrique
def suiteGeo(uo, raison, nbTerme):
	terme = 0
	valeurRang = uo
	while(terme <= nbTerme):
		print("U(" + str(terme) + ") = " + str(valeurRang))
		valeurRang *= raison
		terme+=1

# Inverse l'ordre des termes d'une liste
def inverList(liste):
    listeInverse = [];
    lenght = len(liste)
    for i in range(0, lenght):
        listeInverse.append(liste[lenght - 1 - i])
    return listeInverse ;
	
#Converti une liste en binaire vers un nombre décimal
def convertBinaire(binaire):
    # La valeur en base de 10 du nombre binaire
    nombre = 0;
    
    # La longueur de la liste binaire, [1, 0] renvoie 2.
    longueur = len(binaire)

    for i in range(0, longueur):
        if(binaire[i] != 0 and binaire[i] != 1):
            nombre = 0;
            break;
		# Algorythme vu en cours, EX: '1001' en binaire est égal à " (1 * 2^0) + (0 * 2^1) + (0 * 2^2) + (1 * 2^3)  "
        nombre += binaire[longueur - 1 - i] * (2**i)

    return nombre;

