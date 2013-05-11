#Exercise 5
#Create at least two interesting car surfaces and add them to the mock-up.

from pyplasm import *
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
cerchioneinterno=COLOR(Color4f([1.0, 0.0, 1.0, 1.0]))(cerchioneinterno)

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
#VIEW(ex3)




raggio_interno=0.35
raggio_esterno=0.5
lunghezza_tubolore=0.035
raggio_tubolore=0.075
raggio_disco=0.15
spessore_disco=0.025



dom2d=PROD([INTERVALS(1)(10),INTERVALS(1)(10)])
dom1d=INTERVALS(1)(10)


gommaesterna=TORUS([raggio_interno,raggio_esterno])([12,12])
gommaesterna=COLOR(BLACK)(gommaesterna)

disco=CYLINDER([raggio_disco,spessore_disco])(12)
disco=T([3])(-(spessore_disco/2))(disco)
disco=COLOR(GRAY)(disco)
tubo=CYLINDER([raggio_tubolore,lunghezza_tubolore])(12)
tubo=T([3])(-(lunghezza_tubolore/2))(tubo)
cerchiointerno=DIFFERENCE([disco,tubo])
cerchiointerno=COLOR(Color4f([0.0, 1.0, 1.0, 1.0]))(cerchiointerno)
tubocentro=CYLINDER([raggio_tubolore,spessore_disco-0.01])(12)
tubocentro=T([3])(-(spessore_disco/2)+0.005)(tubocentro)
tubocentro=COLOR(BLACK)(tubocentro)


disco1=CYLINDER([0.01,0.001])(6)
disco1=T([1])([raggio_disco*(0.66)])(disco1)
dischi=STRUCT(NN(12)([disco1,ROTATE([1,2])(2*PI/(6))]))
dischi=T([3])([-spessore_disco])(dischi)
dischi=COLOR(BLACK)(dischi)



#vol_x1

linea_vol1=[[0.15,0,0],[0.25,0.05,0]]
linea_vol2=[[0.10,0+0.10,0],[0.25,0.05+0.10,0]]
linea_vol1z=[[0.15,0,spessore_disco],[0.25,0.05,spessore_disco]]
linea_vol2z=[[0.10,0+0.10,spessore_disco],[0.25,0.05+0.10,spessore_disco]]
curva_vol1=BEZIER(S1)(linea_vol1)
curva_vol2=BEZIER(S1)(linea_vol2)
curva_vol1z=BEZIER(S1)(linea_vol1z)
curva_vol2z=BEZIER(S1)(linea_vol2z)	
mapping_vol_tot1=BEZIER(S2)([curva_vol1,curva_vol2,curva_vol2z,curva_vol1z,curva_vol1])
vol_x1=MAP(mapping_vol_tot1)(dom2d)
vol_x1=T([3])([-spessore_disco/2])(vol_x1)
vol_x1=COLOR(Color4f([0.0, 1.0, 1.0, 1.0]))(vol_x1)


linea_vol1n=[[0.25,0.15,0],[0.35,0.15,0]]
linea_vol2n=[[0.25,0.15+0.10,0],[0.35,0.15+0.10,0]]
linea_vol1zn=[[0.25,0.15,spessore_disco],[0.35,0.15,spessore_disco]]
linea_vol2zn=[[0.25,0.15+0.10,spessore_disco],[0.35,0.15+0.10,spessore_disco]]
curva_vol1n=BEZIER(S1)(linea_vol1n)
curva_vol2n=BEZIER(S1)(linea_vol2n)
curva_vol1zn=BEZIER(S1)(linea_vol1zn)
curva_vol2zn=BEZIER(S1)(linea_vol2zn)	
mapping_vol_tot1n=BEZIER(S2)([curva_vol1n,curva_vol2n,curva_vol2zn,curva_vol1zn,curva_vol1n])
vol_x1n=MAP(mapping_vol_tot1n)(dom2d)
vol_x1n=T([3])([-spessore_disco/2])(vol_x1n)
vol_x1n=COLOR(BLACK)(vol_x1n)
vol_x1n=T([2])([-0.1])(vol_x1n)
vol_x1=STRUCT([vol_x1,vol_x1n])
#VIEW(vol_x1)


#vol_x3

linea_vol31=[[0.05,-0.12,0],[0.05,-0.25,0]]
linea_vol32=[[-0.05,-0.12,0],[-0.05,-0.25,0]]
linea_vol31z=[[0.05,-0.15,spessore_disco],[0.05,-0.25,spessore_disco]]
linea_vol32z=[[-0.05,-0.15,spessore_disco],[-0.05,-0.25,spessore_disco]]


curva_vol111=BEZIER(S1)(linea_vol31)
curva_vol211=BEZIER(S1)(linea_vol32)

curva_vol111z=BEZIER(S1)(linea_vol31z)
curva_vol211z=BEZIER(S1)(linea_vol32z)	

mapping_vol_tot3=BEZIER(S2)([curva_vol111,curva_vol211,curva_vol211z,curva_vol111z,curva_vol111])

vol_x3=MAP(mapping_vol_tot3)(dom2d)

vol_x3=T([3])([-spessore_disco/2])(vol_x3)
vol_x3=COLOR(Color4f([0.0, 1.0, 1.0, 1.0]))(vol_x3)



linea_vol31n=[[0.05,-0.25,0],[0.05,-0.35,0]]
linea_vol32n=[[-0.05,-0.25,0],[-0.05,-0.35,0]]
linea_vol31zn=[[0.05,-0.25,spessore_disco],[0.05,-0.35,spessore_disco]]
linea_vol32zn=[[-0.05,-0.25,spessore_disco],[-0.05,-0.35,spessore_disco]]

curva_vol111n=BEZIER(S1)(linea_vol31n)
curva_vol211n=BEZIER(S1)(linea_vol32n)

curva_vol111zn=BEZIER(S1)(linea_vol31zn)
curva_vol211zn=BEZIER(S1)(linea_vol32zn)	

mapping_vol_tot3n=BEZIER(S2)([curva_vol111n,curva_vol211n,curva_vol211zn,curva_vol111zn,curva_vol111n])

vol_x3n=MAP(mapping_vol_tot3n)(dom2d)

vol_x3n=T([3])([-spessore_disco/2])(vol_x3n)

vol_x3n=COLOR(BLACK)(vol_x3n)
vol_x3=STRUCT([vol_x3,vol_x3n])
vol_x3=T([1])([-0.01])(vol_x3)
#VIEW(vol_x3)

vol_x2=S([1])([-1])(vol_x1)
vol=STRUCT([vol_x1,vol_x2,vol_x3])
vol=COLOR(GRAY)(vol)
volantecompleto=STRUCT([gommaesterna,cerchiointerno,vol,tubocentro,dischi])


volantecompleto=ROTATE([2,3])(PI/2)(volantecompleto)
volantecompleto=ROTATE([1,2])(PI/2)(volantecompleto)

volantecompleto=ROTATE([1,2])(PI/2)(volantecompleto)

#VIEW(volantecompleto)


volantecompleto=T([2])([(+12.5/2)-5.6])(volantecompleto)
volantecompleto=T([1])([-1.2])(volantecompleto)
volantecompleto=T([3])([1.9])(volantecompleto)
volantecompleto=S([1,2,3])([0.6,0.6,0.6])(volantecompleto)
ex4=STRUCT([linea,ruotaavnti,ruotadietro,volantecompleto])
#VIEW(ex4)





#parabrezza auto

dom2D = PROD([INTERVALS(1)(36),INTERVALS(1)(36)])

punti1 = [[0,-1.8/30,0.2],[0,1.6,0.2],[0,2,0],[0,2,0]]
curva1 = CUBICHERMITE(S1)(punti1);

punti2 = [[2.1,0,0],[0.65*2.1,1.8,0],[0,1.8,0],[-2.1/2,1.2*1.8,0]]
curva2 = CUBICHERMITE(S1)(punti2);

curva_completa = [curva1,curva2,[2.1,0,0],[2.1,0,-0.2]]


parabrezza_superficie = CUBICHERMITE(S2)(curva_completa);
parabrezza_rettangolare1 = MAP(parabrezza_superficie)(dom2D);
parabrezza_rettangolare2 = S(1)(-1)(parabrezza_rettangolare1)



parabrezza_rettangolare = STRUCT([parabrezza_rettangolare1,parabrezza_rettangolare2])
parabrezza_rettangolare = COLOR(Color4f([0.0, 1.0, 1.0, 1.0]))(parabrezza_rettangolare)

parabrezza_rettangolare = R([2,3])(PI/12)(parabrezza_rettangolare)

#parabrezza_rettangolare = R([2,3])(PI/12)(parabrezza_rettangolare)

parabrezza_rettangolare = R([1,2])(PI)(parabrezza_rettangolare)


parabrezza_rettangolare=T([2])([(12.5/2)-4.3])(parabrezza_rettangolare)
#parabrezza_rettangolare=T([2])([0.1])(parabrezza_rettangolare)

parabrezza_rettangolare=T([3])([1.85])(parabrezza_rettangolare)
parabrezza_rettangolare=S([1])([0.85])(parabrezza_rettangolare)
parabrezza_rettangolare=T([1])([0.10])(parabrezza_rettangolare)

#VIEW(parabrezza_rettangolare)



#marmitta doppia

profile=[[1,0,1],[1,0,3],[1.5,0,6],[2,0,11]]
dom2dcircle=PROD([INTERVALS(1)(10),INTERVALS(2*PI)(36)])
profile_curva= BEZIER(S1)(profile)
marmitta=MAP(ROTATIONALSURFACE(profile_curva))(dom2dcircle)
marmitta=T([3])([-1])(marmitta)
marmitta=S([1,2,3])([0.1,0.1,0.1])(marmitta)
marmitta=R([1,3])(-PI/2)(marmitta)
marmitta=S([1])([0.25])(marmitta)


marmitta2=T([2])([-0.4])(marmitta)
marmittadoppia=STRUCT([marmitta,marmitta2])
marmittadoppia=T([2])([0.2])(marmittadoppia)
marmittadoppia=ROTATE([1,2])(PI/2)(marmittadoppia)
marmittadoppia=ROTATE([2,3])(PI)(marmittadoppia)

marmittadoppia=COLOR(GRAY)(marmittadoppia)
marmittadoppia1=marmittadoppia
marmittadoppia2=T([1])([1.4])(marmittadoppia)
marmittadoppia1=T([1])([-1.4])(marmittadoppia)

#VIEW(marmittadoppia)
marmittadoppia=STRUCT([marmittadoppia1,marmittadoppia2])
marmittadoppia=T([2])([(-12.5/2)+1.2])(marmittadoppia)



#specchietto
dom2d = PROD([INTERVALS(1)(10),INTERVALS(1)(10)])

punti1 = [[0,0.5,0],[0.1,0.7,0],[0.6,0.75,0],[0.9,0.7,0],[1,0.5,0]]
punti2 = [[0,0.5,0],[-0.13,-0.13,0],[0.13,0.15,0],[0.6,-0.13,0],[1,0,0],[1,0.5,0]]

curve1 = BEZIER(S1)(punti1)
curve2 = BEZIER(S1)(punti2)

specchietto_vetro = BEZIER(S2)([curve1,curve2])
specchietto_vetro = MAP(specchietto_vetro)(dom2d)
specchietto_vetro = COLOR(Color4f([0.0, 1.0, 1.0, 1.0]))(specchietto_vetro)
specchietto_vetro = T([1,2])([0.03,-0.02])(specchietto_vetro)
	
punti1_retro = [[0,0.5,0],[0.25,0.5,0.25],[0.5,0.5,0.5],[0.75,0.5,0.25],[1,0.5,0]]
punti2_retro = [[0,0.5,0],[0.25,0.42,0.25],[0.5,0.35,0.5],[0.75,0.42,0.25],[1,0.5,0]]

curva1_retro = BEZIER(S1)(punti1_retro)
curva2_retro = BEZIER(S1)(punti2_retro)

specchietto_retro = BEZIER(S2)([curve1,curva1_retro,curva2_retro,curve2])
specchietto_retro = MAP(specchietto_retro)(dom2d)
specchietto_retro = COLOR(Color4f([1.0, 1.0, 0.0, 1.0]))(specchietto_retro)
specchietto_retro = T([1,2])([0.03,-0.02])(specchietto_retro)
	
specchietto = STRUCT([specchietto_vetro,specchietto_retro])
specchietto=S([1,2,3])([0.1,0,1,0.1])(specchietto)
specchietto = R([2,3])(PI/2)(specchietto)
specchietto = STRUCT([specchietto_vetro,specchietto_retro])
specchietto = R([2,3])(PI/2)(specchietto)
specchietto = S([2])([-1])(specchietto)
specchietto1 = T([1,2,3])([2.6+1.4,((12.5/2)-5.7),(1.7-0.5)+1.9])(specchietto)
specchietto1=S([1,2,3])([2,2,1])(specchietto1)
specchietto1=S([1])([0.66])(specchietto1)
specchietto1=S([1])([0.66])(specchietto1)
specchietto1=S([1,2,3])([0.75,0.85,0.5])(specchietto1)

specchietto2 = S([1])([-1])(specchietto1)

specchietto2 = T([1,2])([0.17,0.1])(specchietto2)

specchietto=STRUCT([specchietto1,specchietto2])

#VIEW(specchietto)
	

#cofano


dom1d=INTERVALS(1)(50)
dom2D = PROD([INTERVALS(1)(50),INTERVALS(1)(50)])

punti1 = [[-1.2,0,0],[2.6,0,0]]

punti2=[[-1.2,0.035,0.3],[2.6,0.035,0.3],[3.7,0.035,0.3]]

punti2b=[[0.2,1.2,0.35],[4.2,1.2,0.35]]
punti3=[[0.2,1.4,0.35],[4.2,1.4,0.35]]
punti4=[[0.2,2.6,0.4],[4.4,2.6,0.4]]



punti1=BEZIER(S1)(punti1)

punti2=BEZIER(S1)(punti2)
punti2b=BEZIER(S1)(punti2b)


punti3=BEZIER(S1)(punti3)

punti4=BEZIER(S1)(punti4)




cofano1=BEZIER(S2)([punti1,punti2,punti2b,punti3,punti4])

cofano1= MAP(cofano1)(dom2D)
cofano2=S([2])([-1])(cofano1)
cofano2=T([2])([5.2])(cofano2)
cofano=STRUCT([cofano1,cofano2])
cofano=COLOR(Color4f([1.0, 1.0, 0.0, 1.0]))(cofano)
cofano=S([1])([0.99])(cofano)
#VIEW(cofano)

#cofano=ROTATE([1,3])(PI/2)(cofano)

cofano=ROTATE([1,2])(-PI/2)(cofano)
cofano=S([2])([-1])(cofano)
cofano = ROTATE([2,3])(-PI/20)(cofano)
cofano=T([2])([(12.5/2)-4.5+0.5])(cofano)
cofano=T([3])([1.5])(cofano)
cofano=T([1])([-2.5])(cofano)



#sedere


dom1d=INTERVALS(1)(10)
dom2D = PROD([INTERVALS(1)(10),INTERVALS(1)(10)])

sedere2=[[0.4,0,0],[4.6,0,0]]
sedereinclinazione1=[[0.05,-0.40*2,0.2],[4.95,-0.4*2,0.2]]
sedereinclinazione2=[[0.1,-0.40*2,0.4],[4.9,-0.4*2,0.4]]
sedereinclinazione3=[[0.1,-0.50*2.4,1.45],[4.9,-0.5*2.4,1.45]]
sedere4=[[0,-0.5*2.4,1.5],[5,-0.5*2.4,1.5]]


sedere2=BEZIER(S1)(sedere2)
sedere4=BEZIER(S1)(sedere4)
sedereinclinazione1=BEZIER(S1)(sedereinclinazione1)
sedereinclinazione2=BEZIER(S1)(sedereinclinazione2)
sedereinclinazione3=BEZIER(S1)(sedereinclinazione3)

sedere=BEZIER(S2)([sedere2,sedereinclinazione1,sedereinclinazione2,sedereinclinazione3,sedere4])
sedere= MAP(sedere)(dom2D)



sedere=COLOR(Color4f([1.0, 1.0, 0.0, 1.0]))(sedere)
sedere=S([1])([0.99])(sedere)
#VIEW(sedere)
sedere=T([1,2,3])([-2.5,-(12.5/2)+1.2,0.1])(sedere)

ex5=STRUCT([linea,ruotaavnti,ruotadietro,volantecompleto,marmittadoppia,parabrezza_rettangolare,cofano,specchietto,sedere])
VIEW(ex5)