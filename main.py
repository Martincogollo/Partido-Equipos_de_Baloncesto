contgeneral=0
contchigaco=0
contangeles=0
contlibre_chica=0
contdoble_chica=0
conttriple_chica=0
contlibre_angeles=0
contdoble_angeles=0
conttriple_angeles=0
#contgeneral=contgeneral+1
num_equipo=int(input('Ingresar [1]Chicago Bulls o [2]Angeles Lakers: '))
while num_equipo!=0:
  cant_pts=int(input('Digite el tipo de lanzamineto\n [1]lanzamiento libre\n [2]un doble\n [3]un triple\n: '))
  if cant_pts==1 and num_equipo==1:
    contlibre_chica+=1
    contchigaco+=1
    contgeneral+=0
  elif cant_pts==2 and num_equipo==1:
   contdoble_chica+=1
   contchigaco+=1
   contgeneral+=1
  elif cant_pts==3 and num_equipo==1:
   conttriple_chica+=1
   contchigaco+=1
   contgeneral+=1
  elif cant_pts==1 and  num_equipo==2:
   contlibre_angeles+=1
   contangeles+=1
   contgeneral+=1
  elif cant_pts==2 and num_equipo==2:
   contdoble_angeles+=1
   contangeles+=1
   contgeneral+=1
  elif cant_pts==3 and num_equipo==2:
   conttriple_angeles+=1 
   contangeles+=1
   contgeneral+=1
  num_equipo=int(input('Ingresar [1]Chicago Bulls o [2]Angeles Lakers: '))
print('Cantidad de tiros libre de Chicago Bulls: ',contlibre_chica)
print('Cantidad de tiros libre de Angeles Lakers: ',contlibre_angeles)
print('Cantidad de tiros dobles de Chicago Bulls: ',contdoble_chica)
print('Cantidad de tiros dobles de Angeles Lakers: ',contdoble_angeles)
print('Cantidad de tiros triples de Chicago Bulls : ',conttriple_chica)
print('Cantidad de tiros triples de Angeles Lakers: ',conttriple_angeles)
print('Total de lanzaminetos del equipo Chicago Bulls: ',contchigaco)
print('Total de lanzaminetos del equipo Angeles Lakers: ',contangeles)
print('Total de lanzaminetos: ',contgeneral)
puntos_chica=(contlibre_chica*1)+(contdoble_chica*2)+(conttriple_chica*3)
puntos_angeles=(contlibre_angeles*1)+(contdoble_angeles*2)+(conttriple_angeles*3)
print('total de puntos del equipo Chicago Bulls: ',puntos_chica)
print('total de puntos del equipo Angeles Lakers: ',puntos_angeles)
if puntos_chica>puntos_angeles:
  for letra in'Equipo Ganador Chicago Bulls':
   print(letra,end=' ')
elif puntos_chica==puntos_angeles:
  for letra in'Tiempo Extra':
   print(letra,end=' ')
else:
  for letra in'Equipo Ganador  Angeles Lakers':
   print(letra ,end=' ')