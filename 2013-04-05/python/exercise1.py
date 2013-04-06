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
cuboid3Est1 = (T([1])([2*(0.5+4.7)])(cuboid)
cuboid3Est2 = (T([1])([4*(0.5+4.7)])(cuboid)
cuboid3Est= STRUCT([cuboid3Est1,cuboid3Est2])
pillars3 = STRUCT([cuboid3Small1,cuboid3Small2,cuboid3Ovest,cuboid3Est])
pillars3=T([3])([3*(h+solaio)])(pillars3)


VIEW(STRUCT([pillars0,pillars1,pillars2,pillars3]))
