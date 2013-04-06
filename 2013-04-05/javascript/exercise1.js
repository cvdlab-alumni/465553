//Exercise 1

/*Define, with names pillars0, pillars1, pillars2, and pillars3, the models of pillars of the 4 house floors,
and put them into the STRUCT of an initial building model.
*/

//altezza piano  
var h=3
//altezza solaio 
var solaio=0.2


//cylinder and cube
var cylinder = CYL_SURFACE([0.25,h])([100,1])
var cuboid = CUBOID([0.5,0.5,h])
var cuboidSmall = CUBOID([0.25,0.25,h])

//traslate the cylinder
var cylinder = T([0,1])([0.25,0.25])(cylinder)


//pillars0

var cuboid0Est1 = T([0,1])([0.5+2.2,0.5+10.2])(cuboid)
var cuboid0Est2 = T([1])([10.2+0.5])(STRUCT(REPLICA(3)([T([0])([0.5+5]),cuboid])))
var cuboidTot0 = STRUCT([cuboid0Est1,cuboid0Est2])

var cylinder0Ovest = STRUCT(REPLICA(5)([cylinder,T([0])([0.5+5])]))
cylinder0Est = T([1])([0.5+10.2])(cylinder)
cylinderTot0= STRUCT([cylinder0Est,cylinder0Ovest])

pillars0 = STRUCT([cylinderTot0,cuboidTot0])

DRAW(pillars0)
HIDE(pillars0)

//pillars1

var cuboid1Est1= STRUCT(REPLICA(5)([cuboid,T([0])([0.5+5])]))
var cuboid1Est2 = T([1])([10.2+0.5])(STRUCT(REPLICA(3)([cuboid,T([0])([0.5+5])])))
var cuboid1Ovest = T([0,1])([4*(0.5+5),0.5+10.2])(cuboid)
var cuboid1Small = T([0,1])([0.5+0.9,0.5+10.2])(cuboidSmall)
var cuboidTot1 = STRUCT([cuboid1Ovest,cuboid1Est1,cuboid1Est2, cuboid1Small])

var cylinder1Ovest = T([0,1])([3*(0.5+5),0.5+10.2])(cylinder)


var pillars1 = STRUCT([cylinder1Ovest,cuboidTot1])
var pillars1 =T([2])([h+solaio])(pillars1)


DRAW(pillars1)
HIDE(pillars1)
//pillars2

var cuboid2Ovest = T([1])([0.5+10.2])(STRUCT(REPLICA(5)([cuboid,T([0])([5+0.5])])))
var cuboid2Est1= STRUCT([cuboid,STRUCT(REPLICA(2)([T([0])([0.5+5]),cuboid]))])
var cuboid2Est = T([0])([4*(0.5+5)])(cuboid)
var cuboid2Est= STRUCT([cuboid2Est1,cuboid2Est])

var pillars2 = STRUCT([cuboid2Ovest,cuboid2Est])
var pillars2=T([2])([2*(h+solaio)])(pillars2)


DRAW(pillars2)
HIDE(pillars2)
// pillars3

var cuboid3Small1 = T([1])([0.5+10.2+0.25])(cuboidSmall)
var cuboid3Small2 = T([0,1])([0.5+5,0.5+10.2+0.25])(cuboidSmall)
var cuboid3Ovest = T([0,1])([2*(0.5+5),0.5+10.2])(cuboid)
var cuboid3Ovest=STRUCT(REPLICA(3)([cuboid3Ovest,T([0])([0.5+5])]))
var cuboid3Est1 = T([0])([2*(0.5+5)])(cuboid)
var cuboid3Est2 = T([0])([4*(0.5+5)])(cuboid)
var cuboid3Est= STRUCT([cuboid3Est1,cuboid3Est2])
var pillars3 = STRUCT([cuboid3Small1,cuboid3Small2,cuboid3Ovest,cuboid3Est])
var pillars3=T([2])([3*(h+solaio)])(pillars3)


DRAW(pillars3)
HIDE(pillars3)
var pillars=STRUCT([pillars0,pillars1,pillars2,pillars3])

DRAW(pillars)
