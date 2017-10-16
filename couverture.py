import math

print('--- SAISIR LONGUEUR ---')
longueur = float(input())
print('--- SAISIR LARGUEUR ---')
largueur = float(input())
print('--- SAISIR ANGLE DEGRES ---')
angle = float(input())
angle_radian = math.radians(angle)
hypothenuse = largueur/math.cos(angle_radian)
surface_couverture = hypothenuse * longueur
print('--- SURFACE DE COUVERTURE : ---')
print(surface_couverture)

print('AVEZ VOUS DE LA SURFACE A DEDUIRE ? Oui/Non')

reponse1 = input()

if (reponse1 == 'Oui'):
    print('--- SAISIR LONGUEUR ---')
    longueur = float(input())
    print('--- SAISIR LARGUEUR ---')
    largueur = float(input())
    print('--- SAISIR ANGLE DEGRES ---')
    angle = float(input())
    angle_radian = math.radians(angle)
    hypothenuse = largueur/math.cos(angle_radian)
    surface_couverture_deduire = hypothenuse * longueur
    print(surface_couverture_deduire)
    print('SURFACE DE COUVERTURE TOTALE')
    total = surface_couverture - surface_couverture_deduire
    total_r = round(total,2)
    print(total_r, 'm²')
    


