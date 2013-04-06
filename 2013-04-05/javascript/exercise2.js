//Exercise 2

//Define plan by plan, with names floor0, floor1, floor2, floor3, and floor4,
// the 5 models of horizontal partitions, and add them to the STRUCT of the building model.
//

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
HIDE(pillars)

//floors0
var piano=solaio

var floors0=SIMPLEX_GRID([[21.25],[13.8],[piano]])
var floors0=T([2])([-piano])(floors0)

DRAW(floors0)
HIDE(floors0)



//floors 1

var fl11=(SIMPLEX_GRID([[21.25],[4,4.8,2.4],[piano]]))
var fl12=(SIMPLEX_GRID([[9,-3.5,(21.25-(3.5+9))],[-4,4.8,-2.4],[piano]]))
var fl13=T([0,1])([9+1.6,4+4.8-0.5])((SIMPLEX_GRID([[(3.5-1.6)],[0.5],[piano]])))
var fl14=T([0,1])([-2.8,11])((SIMPLEX_GRID([[4.8,-10,(2.8+21.25-10-4.8)],[13.8-4-4.8-2.4],[piano]])))
var floors1=STRUCT([fl11,fl12,fl13,fl14])
var floors1=T([2])([h+piano])(floors1)
DRAW(floors1)
HIDE(floors1)

//floors 2


var fl21=T([0,1])([21.25-6.3,13.8-2.8])((SIMPLEX_GRID([[6.3],[2.4],[piano]])))
var fl22=EXTRUDE([piano]) (SIMPLICIAL_COMPLEX([[21.25-11.4,0],[21.25,0],[21.25,(4+4.8+2.4)],[9.6,(4+4.8+2.4)]])([[0,1,2],[2,3,0]]))
var floors2=STRUCT([fl21,fl22])
var floors2=T([2])([2*(h+piano)])(floors2)
DRAW(floors2)
HIDE(floors2)

//floors 3

var fl31=(SIMPLEX_GRID([[-11.1,(21.25-11.1)],[(13.8-2.8)],[piano]]))

var fl32=(SIMPLEX_GRID([[-11.1,-6.8,(21.25-11.1-6.8)],[-(13.8-2.8),2.8],[piano]]))

var fl33=(SIMPLEX_GRID([[11.1],[13.8],[piano]]))

var floors3=STRUCT([fl31,fl32,fl33])
var floors3=T([2])([3*(h+piano)])(floors3)
DRAW(floors3)
HIDE(floors3)





//floors 4


var fl41=(SIMPLEX_GRID([[(21.25-10.5)],[(3.8)],[piano]]))
var fl41=T([1])([10])(fl41)
var fl42=(SIMPLEX_GRID([[-(10+0.5),21.25-10],[13.8],[piano]]))
var floors4=STRUCT([fl41,fl42])
var floors4=T([2])([4*(h+piano)])(floors4)
DRAW(floors4)
HIDE(floors4)

var floors=STRUCT([floors0,floors1,floors2,floors3,floors4])
var model=STRUCT([floors,pillars])
var model=T([2])([piano])(model)

DRAW(model)