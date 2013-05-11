#Exercise 3
#Generate a model of a racing car wheels (see, e.g. here),
#and mount four wheel instances in the 2.5D car mock-up.


from pyplasm import *
import sys
sys.path.append("/home/matteomagnus/github/larpy")

from lar import *
from scipy import *

#Funzione per generare una griglia di complessi simpliciali"""
def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])
	
domain_grid = GRID([25,25])
dominio2D = MAP([S2,S1])(GRID([25,25]))


dominio2D=PROD([INTERVALS(1)(10),INTERVALS(1)(10)])

dom1d=INTERVALS(1)(10)



linea1x=[[0.4,0],[0.02,1.2],[0.2,-0.1],[0.4,-0,1]]
linea2x=[[0.4,0],[4.6,0]]
linea3x=[[4.6,0],[4.98,1.2],[0,-0.1],[-0.5,0,3]]

linea1x = CUBICHERMITE(S1)(linea1x);
linea1x = MAP(linea1x)(dom1d);

linea2x=BEZIER(S1)(linea2x)
linea2x=MAP(linea2x)(dom1d)

linea3x = CUBICHERMITE(S1)(linea3x);
linea3x = MAP(linea3x)(dom1d);

linea4x=[[4.98,1.2],[4.6,1.8],[3.8,2.5]]
linea5x=[[3.8,2.5],[1.2,2.5]]
linea6x=[[1.2,2.5],[0.4,1.9],[0.02,1.2]]

linea4x=BEZIER(S1)(linea4x)
linea4x=MAP(linea4x)(dom1d)
linea5x=BEZIER(S1)(linea5x)
linea5x=MAP(linea5x)(dom1d)
linea6x=BEZIER(S1)(linea6x)
linea6x=MAP(linea6x)(dom1d)

lineax=STRUCT([linea1x,linea2x,linea3x,linea4x,linea5x,linea6x])

lineax=ROTATE([2,3])(PI/2)(lineax)
lineax=T([1])([-2.5])(lineax)
#VIEW(lineax)








#linea y=0

linea1y=[[0,1.6],[0.4,0.3],[1.3,0.1]]
linea2y=[[0,0.06],[0,0.66],[1,0.66],[1,0]]
linea3y=[[3.5,0],[3.5+5.1,0]]
linea4y=[[0,0.025],[0,0.66],[1,0.66],[1,0]]
linea5y=[[10.8,0],[12.1,0.5],[12.46,0.7],[12.5,0.85]]
linea6y=[[8.1,1.8],[11.5,1.6],[11.9,0.7],[12.2,1.3],[12.5,0.8]]
linea7y=[[8.1,1.8],[6.5,2.5]]
linea8y=[[6.5,2.5],[4.2,2.4]]
linea9y=[[1.2,1.8],[4.2,2.4]]
linea10y=[[1.2,1.8],[1,1.6],[0,1.6]]


linea1y=BEZIER(S1)(linea1y)
linea1y=MAP(linea1y)(dom1d)

linea2y=BEZIER(S1)(linea2y)
linea2y=MAP(linea2y)(dom1d)
linea2y=S([1,2])([2.2,1.5])(linea2y)
linea2y=T([1])([1.3])(linea2y)


linea3y=BEZIER(S1)(linea3y)
linea3y=MAP(linea3y)(dom1d)

linea4y=BEZIER(S1)(linea4y)
linea4y=MAP(linea4y)(dom1d)
linea4y=S([1,2])([2.2,1.5])(linea4y)
linea4y=T([1])([5.1+3.5])(linea4y)


linea5y=BEZIER(S1)(linea5y)
linea5y=MAP(linea5y)(dom1d)


linea6y=BEZIER(S1)(linea6y)
linea6y=MAP(linea6y)(dom1d)

linea7y=BEZIER(S1)(linea7y)
linea7y=MAP(linea7y)(dom1d)

linea8y=BEZIER(S1)(linea8y)
linea8y=MAP(linea8y)(dom1d)


linea9y=BEZIER(S1)(linea9y)
linea9y=MAP(linea9y)(dom1d)

linea10y=BEZIER(S1)(linea10y)
linea10y=MAP(linea10y)(dom1d)

lineay=STRUCT([linea1y,linea2y,linea3y,linea4y,linea5y,linea6y,linea7y,linea8y,linea9y,linea10y])
lineay=ROTATE([2,3])(PI/2)(lineay)
lineay=ROTATE([1,2])(PI/2)(lineay)
lineay=T([2])([-12.5/2])(lineay)
#VIEW(lineay)


#profilo z=0


linea1z=[[0,2.5],[0,0.6],[0,0.1],[1,0]]
linea2z=[[1,0],[10.5,0]]
linea3z=[[10.5,0],[11.4,0.4],[12.3,0.7],[12.5,2.5]]

linea1z=BEZIER(S1)(linea1z)
linea1z=MAP(linea1z)(dom1d)

linea2z=BEZIER(S1)(linea2z)
linea2z=MAP(linea2z)(dom1d)


linea3z=BEZIER(S1)(linea3z)
linea3z=MAP(linea3z)(dom1d)



lineaz1=STRUCT([linea1z,linea2z,linea3z])
lineaz2=S([2])([-1])(lineaz1)
lineaz2=T([2])([5])(lineaz2)
lineaz=STRUCT([lineaz1,lineaz2])



lineaz=ROTATE([2,3])(PI/2)(lineaz)
lineaz=ROTATE([1,2])(-PI/2)(lineaz)
lineaz=ROTATE([2,3])(-PI)(lineaz)
lineaz=ROTATE([1,3])(-PI/2)(lineaz)
lineaz=T([1,2])([2.5,-12.5/2])(lineaz)

#VIEW(lineaz)







linea=STRUCT([lineax,lineay,lineaz])
#VIEW(linea)









raggio_gomma_interno=0.35
raggio_gomma_esterno=0.5
lunghezza_tubolore=0.035
raggio_tubolore=0.075
raggio_disco=0.15
spessore_disco=0.025
numero_raggi=12

pneumatic=TORUS([raggio_gomma_interno,raggio_gomma_esterno])([12,12])
pneumatic=COLOR(BLACK)(pneumatic)
pneumatic_interno=TORUS([(raggio_gomma_interno-0.05),raggio_gomma_interno])([12,12])
pneumatic_interno=COLOR(Color4f([1.0, 0.0, 1.0, 1.0]))(pneumatic_interno)
disco=CYLINDER([raggio_disco,spessore_disco])(12)
disco=T([3])(-(spessore_disco/2))(disco)
disco=COLOR(Color4f([1.0, 0.0, 1.0, 1.0]))(disco)
tubo=CYLINDER([raggio_tubolore,lunghezza_tubolore])(12)
tubo=T([3])(-(lunghezza_tubolore/2))(tubo)
cerchioneinterno=DIFFERENCE([disco,tubo])
cerchioneinterno=COLOR(RED)(cerchioneinterno)

linea_raggio1=[[0,0,0],[0.15,0.05,0.10],[raggio_gomma_interno-0.05-raggio_disco,0,0]]
linea_raggio2=[[0-0.08,0+0.10,0],[0.15,0.05+0.10,0.10],[raggio_gomma_interno-0.05-raggio_disco,0+0.10,0]]
linea_raggio1z=[[0,0,0+spessore_disco],[0.15,0.05,0.10+spessore_disco],[raggio_gomma_interno-0.05-raggio_disco,0,0+spessore_disco]]
linea_raggio2z=[[0-0.08,0+0.10,0+spessore_disco],[0.15,0.05+0.10,0.10+spessore_disco],[raggio_gomma_interno-0.05-raggio_disco,0+0.10,0+spessore_disco]]


curva_raggio1=BEZIER(S1)(linea_raggio1)
curva_raggio2=BEZIER(S1)(linea_raggio2)

curva_raggio1z=BEZIER(S1)(linea_raggio1z)
curva_raggio2z=BEZIER(S1)(linea_raggio2z)

mapping_raggio=BEZIER(S2)([curva_raggio1,curva_raggio2,curva_raggio2z,curva_raggio1z,curva_raggio1])

raggiosingolo=MAP(mapping_raggio)(dominio2D)

raggiosingolo=T([3])([-spessore_disco/2])(raggiosingolo)


raggiosingolo=T([1])(raggio_disco)(raggiosingolo)
raggi=STRUCT(NN(numero_raggi)([raggiosingolo,ROTATE([1,2])(2*PI/(numero_raggi))]))
raggi=COLOR(Color4f([1.0, 0.0, 1.0, 1.0]))(raggi)


ruotacompleta=STRUCT([pneumatic,pneumatic_interno,cerchioneinterno,raggi])

ruotacompleta=ROTATE([2,3])(PI/2)(ruotacompleta)
ruotacompleta=ROTATE([1,2])(PI/2)(ruotacompleta)
#VIEW(ruotacompleta)


ruota1=T([1])([-2.5-(0.15/2)])(ruotacompleta)
ruota2=T([1])([5+(0.15)])(ruota1)


#ruota1=T([1])([(-12.5/2)+2.5])(ruotacompleta)
#ruota2=T([1])([(-12.5/2)+9.7])(ruotacompleta)

ruota=STRUCT([ruota1,ruota2])
ruotadietro=T([2])([(-12.5/2)+2.5])(ruota)
ruotaavnti=S([2])([-1])(ruota)
ruotaavnti=T([2])([(12.5/2)-2.7])(ruotaavnti)
ex3=STRUCT([linea,ruotaavnti,ruotadietro])
VIEW(ex3)