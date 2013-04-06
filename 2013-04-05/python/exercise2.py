#Exercise 2

#Define plan by plan, with names floor0, floor1, floor2, floor3, and floor4,
# the 5 models of horizontal partitions, and add them to the STRUCT of the building model.
#

from pyplasm import *

#altezza piano  
h=3
#altezza solaio 
solaio=0.2


#cylinder and cube
cylinder = T([1,2])([0.25,0.25])(CYLINDER([0.25,h])(36))
cuboid = CUBOID([0.5,0.5,h])
cuboidSmall = CUBOID([0.25,0.25,h])



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
fl14=T([1,2])([-2.8,11])(INSR(PROD)(AA(QUOTE)([[4.8,-10,(2.8+21.25-10-4.8)],[13.8-4-4.8-2.4],[piano]])))
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
building=STRUCT([floors,pillars])
building=T(3)((piano))(building)
VIEW(building)