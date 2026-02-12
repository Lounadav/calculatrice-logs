import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programme démarré")
def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        logging.error("Erreur : division par zéro")
        return None
    return a / b

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
logging.info("Lancement de l'addition")
print("Résultat de l'addition :", resultat_addition)

resultat_division = division(x, y)
if resultat_division is not None:
    logging.info("Lancement de la division")
    print("Résultat de la division :", resultat_division)
else:
    print("Division impossible")

logging.info("Programme terminé")