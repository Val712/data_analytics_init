import statistics
def analyser_ventes(transactions):
    ventes_valides = []
    for t in transactions:
        if t > 0:
            ventes_valides.append(t)
    taille = len(ventes_valides)
    somme = sum(ventes_valides)
    moyenne = somme/taille
    mediane = statistics.median(ventes_valides)
    ecart_type = round(statistics.pstdev(ventes_valides), 2)
    maximum = max(ventes_valides)
    minimum = min(ventes_valides)
    outliers = [t for t in ventes_valides if t > 2*moyenne]

    #dictionnaire de sortie
    return{
        "nombre_transactions": taille,
        "somme_totale": somme,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "maximum": maximum,
        "minimum": minimum,
        "outliers": outliers,
    }

if __name__ == "__main__":
    ventes_test = [120, 85.5, -50, 300, 0, 90, 150, 2000, -2, 210, 95]
    resultat = analyser_ventes(ventes_test)
    for cle, valeur in resultat.items():
        print(f"{cle}, : {valeur}")

