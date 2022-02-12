from math import sqrt

def racine(a,b,c):
    # initialisation
    resultat = []

    # conversion en float
    a = a*(1.)
    b = b*(1.)
    c = c*(1.)

    # initialisation discriminant
    delta = (b**2) - 4*a*c

    if (a==0):
        resultat.append((-1.)*(c/b))

        return resultat
    else:
        if (delta<0):

            return resultat;
        elif (delta==0):
            resultat.append((-1)*(b/(2*a)))

            return resultat
        else:
            resultat.append(((-b)-sqrt(delta))/(2*a))
            resultat.append(((-b)+sqrt(delta))/(2*a))

            return resultat
