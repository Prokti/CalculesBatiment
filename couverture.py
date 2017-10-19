
import math



def calcule_surface_toit(angle_radian):
    print('--- SAISIR LONGUEUR ---')
    longueur = float(input())
    print('--- SAISIR LARGUEUR ---')
    largueur = float(input())    
    hypothenuse = largueur/math.cos(angle_radian)
    surface_couverture = hypothenuse * longueur
    total3 = round(surface_couverture, 2)
    return total3

total1 = 0
total2 = 0
total3 = 0
total_total = 0


print('--- SAISIR ANGLE DEGRES ---')
angle = float(input())
angle_radian = math.radians(angle)

print('SURFACE DE COUVERTURE ')

total1 = calcule_surface_toit(angle_radian) 
print(total1, 'm² -- A AJOUTER ')


print('AVEZ VOUS DE LA SURFACE A DEDUIRE ? O/N')

reponse1 = input()

if (reponse1 == 'O'):
    total2 = calcule_surface_toit(angle_radian)
    print(total2, 'm² -- A DEDUIRE ')

  

print('AVEZ VOUS DE LA SURFACE A AJOUTER ? O/N')

reponse2 = input()

if (reponse2 =='O'):
    total3 = calcule_surface_toit(angle_radian)
    print(total3, 'm² -- A AJOUTER ')


print("--------TOTAL COUVERTURE--------")
total_total = total1 + total3 - total2
print(total_total, ' m²')

input('APPUYER SUE UNE TOUCHE POUR FERMER')


