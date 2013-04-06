#Exercise 4

from pyplasm import *

#altezza piano  
h=3
#altezza solaio 
solaio=0.2


#cylinder and cube
cylinder = T([1,2])([0.25,0.25])(CYLINDER([0.25,h])(36))
cuboid = CUBOID([0.5,0.5,h])
cuboidSmall = CUBOID([0.25,0.25,h])

#black window

blackwindow=COLOR(BLACK)(INSR(PROD)(AA(QUOTE)([[0.5],[-0.5,9.2],[3,-1.5]])));
blackwindow=STRUCT(NN(2)([blackwindow,(T([3])(solaio+h))]))
blackwindow=T([3])([2*solaio+h])(blackwindow)

#pillars0

cuboid0Ovest = T([1,2])([0.5+2.2,0.5+9.2])(cuboid)
cuboid0Est = T([2])([9.7])(STRUCT(NN(3)([T([1])([0.5+4.7]),cuboid])))
cuboidTot0 = STRUCT([cuboid0Est,cuboid0Ovest])

cylinder0Ovest = STRUCT(NN(5)([cylinder,T([1])([0.5+4.7])]))
cylinder0Est = T([2])([0.5+9.2])(cylinder)
cylinderTot0= STRUCT([cylinder0Est,cylinder0Ovest])

pillars0 = STRUCT([cylinderTot0,cuboidTot0])


#pillars1

cuboid1Est1= STRUCT(NN(5)([cuboid,T([1])([0.5+4.7])]))
cuboid1Est2 = T([2])([9.7])(STRUCT(NN(3)([cuboid,T([1])([0.5+4.7])])))
cuboid1Ovest = T([1,2])([4*(0.5+4.7),0.5+9.2])(cuboid)
cuboid1Small = T([1,2])([0.5+0.9,0.5+9.2])(cuboidSmall)
cuboidTot1 = STRUCT([cuboid1Ovest,cuboid1Est1,cuboid1Est2, cuboid1Small])

cylinder1Ovest = T([1,2])([3*(0.5+4.7),0.5+9.2])(cylinder)


pillars1 = STRUCT([cylinder1Ovest,cuboidTot1])
pillars1 =T([3])([h+solaio])(pillars1)

#pillars2

cuboid2Ovest = T([2])([0.5+9.2])(STRUCT(NN(5)([cuboid,T([1])([4.7+0.5])])))
cuboid2Est1= STRUCT([cuboid,STRUCT(NN(2)([T([1])([0.5+4.7]),cuboid]))])
cuboid2Est = T([1])([4*(0.5+4.7)])(cuboid)
cuboid2Est= STRUCT([cuboid2Est1,cuboid2Est])

pillars2 = STRUCT([cuboid2Ovest,cuboid2Est])
pillars2=T([3])([2*(h+solaio)])(pillars2)

#pillars3

cuboid3Small1 = T([2])([0.5+9.2+0.25])(cuboidSmall)
cuboid3Small2 = T([1,2])([0.5+4.7,0.5+9.2+0.25])(cuboidSmall)
cuboid3Ovest = T([1,2])([2*(0.5+4.7),0.5+9.2])(cuboid)
cuboid3Ovest=STRUCT(NN(3)([cuboid3Ovest,T([1])([0.5+4.7])]))
cuboid3Est1 = T([1])([2*(0.5+4.7)])(cuboid)
cuboid3Est2 = T([1])([4*(0.5+4.7)])(cuboid)
cuboid3Est= STRUCT([cuboid3Est1,cuboid3Est2])
pillars3 = STRUCT([cuboid3Small1,cuboid3Small2,cuboid3Ovest,cuboid3Est])
pillars3=T([3])([3*(h+solaio)])(pillars3)

pillars=STRUCT([pillars0,pillars1,pillars2,pillars3])

#VIEW(pillars)


#floors0
piano=solaio
floors0=INSR(PROD)(AA(QUOTE)([[21.25],[13.8],[piano]]))
floors0=T(3)((-piano))(floors0)
#VIEW(floors0)




#floors 1

fl11=INSR(PROD)(AA(QUOTE)([[21.25],[4,4.8,2.4],[piano]]))
fl12=INSR(PROD)(AA(QUOTE)([[9,-3.5,(21.25-(3.5+9))],[-4,4.8,-2.4],[piano]]))
fl13=T([1,2])([9+1.6,4+4.8-0.5])(INSR(PROD)(AA(QUOTE)([[(3.5-1.6)],[0.5],[piano]])))
fl14=T([1,2])([-2.4,11])(INSR(PROD)(AA(QUOTE)([[4.8,-10,(2.8+21.25-10-4.8)],[13.8-4-4.8-2.4],[piano]])))
floors1=STRUCT([fl11,fl12,fl13,fl14])
floors1=T(3)((h+piano))(floors1)
#VIEW(floors1)


#floors 2


fl21=T([1,2])([21.25-6.3,13.8-2.8])(INSR(PROD)(AA(QUOTE)([[6.3],[2.4],[piano]])))
fl22=(PROD)([MKPOL([[[21.25-11.4,0],[21.25,0],[21.25,(4+4.8+2.4)],[9.6,(4+4.8+2.4)]],[[1,2,3,4]],None]),Q(piano)])

floors2=STRUCT([fl21,fl22])
floors2=T(3)(2*(h+piano))(floors2)
#VIEW(floors2)


#floors 3

fl31=INSR(PROD)(AA(QUOTE)([[-11.1,(21.25-11.1)],[(13.8-2.8)],[piano]]))

fl32=INSR(PROD)(AA(QUOTE)([[-11.1,-6.8,(21.25-11.1-6.8)],[-(13.8-2.8),2.8],[piano]]))

fl33=INSR(PROD)(AA(QUOTE)([[11.1],[13.8],[piano]]))

floors3=STRUCT([fl31,fl32,fl33])
floors3=T(3)(3*(h+piano))(floors3)
#VIEW(floors3)






#floors 4


fl41=INSR(PROD)(AA(QUOTE)([[(21.25-10.5)],[(3.8)],[piano]]))
fl41=T(2)(10)(fl41)
fl42=INSR(PROD)(AA(QUOTE)([[-(10+0.5),21.25-10],[13.8],[piano]]))
floors4=STRUCT([fl41,fl42])
floors4=T(3)(4*(h+piano))(floors4)
#VIEW(floors4)



floors=STRUCT([floors0,floors1,floors2,floors3,floors4])
model=STRUCT([floors,pillars])
model=T(3)((piano))(model)
#VIEW(model)




#north

#floor 1
f1North1=INSR(PROD)(AA(QUOTE)([[-1,1.5],[-20, 0.5],[-3.2,3]]))
f2North1=INSR(PROD)(AA(QUOTE)([[-3,10],[-20, 0.5],[-3.2,1.5]]))

north1=STRUCT([f1North1,f2North1])

#floor 2
f1North2=T([3])([3.2])(f1North1)
f2North2=T([3])([3.2])(f2North1)
north2=STRUCT([f1North2,f2North2])



#floor3
f1North3=T([3])([3.2])(f1North2)
f2North3=T([3])([3.2])(f2North2)
north3=STRUCT([f1North3,f2North3])


north=STRUCT([north1,north2,north3])

#south
#piano3

f1South3=INSR(PROD)(AA(QUOTE)([[2.5,-0.3,10.1],[0.5],[-9.6, 1.5]]))

south3=STRUCT([f1South3])
#floor2
f1south2=INSR(PROD)(AA(QUOTE)([[2.5],[0.5],[-6.4,3]]))
south2=STRUCT([f1south2])

#floor1
f1south1=INSR(PROD)(AA(QUOTE)([[2.2],[0.2],[1.5]]))
f1south1=T([1,2,3])([0.5,-2.3,3.2])(f1south1)

south1=STRUCT([f1south1])


south=STRUCT([south1, south2, south3])

#east
#floor1

f1E1=INSR(PROD)(AA(QUOTE)([[-12.9,0.5],[-0.5,4.5],[-3.2, 3]]))
f2E1=INSR(PROD)(AA(QUOTE)([[-12.9,0.5],[-5.5,4.5],[-3.2, 3]]))
f3E1=INSR(PROD)(AA(QUOTE)([[-12.9,0.5],[-15.5,4.5],[-3.2, 3]]))
f4E1=INSR(PROD)(AA(QUOTE)([[-12.9,0.5],[-10.5,4.5],[-3.2, 1.5]]))

east1=STRUCT([f1E1,f2E1,f3E1,f4E1])

#floor2
f1E2=T([3])([3.2])(f1E1)
f2E2=T([3])([3.2])(f2E1)
f3E2=T([3])([3.2])(f3E1)
f4E2=T([3])([3.2])(f4E1)

east2=STRUCT([f1E2,f2E2,f3E2,f4E2])



#floor3
f1E3=T([3])([3.2])(f3E2)
f2E3=T([3])([3.2])(f4E2)
f3E3=INSR(PROD)(AA(QUOTE)([[-12.9, 0.5],[10],[-9.6, 1.5]]))
cylinder3=CYLINDER([0.1,1.5])(20)
cylinder3=T([1,2,3])([13.15,0.25,9.6+1.5])(cylinder3)

east3=STRUCT([f1E3,f2E3,f3E3,cylinder3])


east=STRUCT([east1, east2,east3])

#west
#floor0
f1west0= INSR(PROD)(AA(QUOTE)([[0.5],[10.5],[3]]))
f2west0=INSR(PROD)(AA(QUOTE)([[0.5],[-10.5, 4.5],[1.7]]))
f3west0=INSR(PROD)(AA(QUOTE)([[0.5],[-10.5,1,-1,2.5],[-1.7,1]]))
f4west0=INSR(PROD)(AA(QUOTE)([[0.5],[-10.5,4.5],[-2.7,0.3]]))
west0=STRUCT([f1west0,f2west0,f4west0,f3west0])

#floor1 
f1west1=T([3])([3.2])(f1west0)
f2west1=INSR(PROD)(AA(QUOTE)([[0.5],[-10.5,4],[-3.2,1.5]]))
f3west1=INSR(PROD)(AA(QUOTE)([[0.5],[-14.5, 6],[-3.2,3]]))


west1=STRUCT([f1west1,f2west1,f3west1])
#floor2
f1west2=T([3])([3.2])(f1west1)
f2west2=INSR(PROD)(AA(QUOTE)([[0.5],[-10.5,4.5],[-6.4, 3]]))
f3west2=INSR(PROD)(AA(QUOTE)([[0.5],[-15, 5.5],[-6.4, 1.5]]))
f4west2=INSR(PROD)(AA(QUOTE)([[0.5],[-15,1,-0.5,1,-0.5,2.5],[-7.9, 1.5]]))

west2=STRUCT([f1west2,f2west2,f3west2,f4west2])



#floor3
f1west3=T([3])([3.2])(f1west2)
f2west3=T([2])([10])(f1west3)
west3=STRUCT([f1west3,f2west3])


west=STRUCT([west0,west1,west2,west3])

faces=STRUCT([north,south,east,west])



faces=R([1,2])((3*(PI/2)))(faces)
faces=T([2])([13.8])(faces)

modelapp = STRUCT([model,faces])
model4=STRUCT( [modelapp,blackwindow])
VIEW(model4)