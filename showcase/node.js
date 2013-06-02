!(function (exports){

  var fs = require('fs');

  var plasm_lib = require('plasm.js');
  var obj = plasm_lib.plasm;
  var fun = plasm_lib.plasm_fun;
  var plasm = obj.plasm;
  var Plasm = obj.Plasm;

  var root = this;

  Object.keys(fun).forEach(function (k) { 
    root[k] = fun[k];
  });

  var p = new Plasm();
  fun.PLASM(p);


  var scmodel = (function () {

 


//Showcase - Code.js - 
//Matteo Riccardi - 465553
//airplane


//Fuselage

var domain1d = INTERVALS(1)(25)
var domain2d =PROD1x1([domain1d,domain1d])

var line13 = BEZIER(S0)([[-2.4,0.8,0],[-2.4,0.8,0]])

var line1 = BEZIER(S0)([[0,0,0],[0,0,1.4],[0,2.4,1.4],[0,2.4,-1.4],[0,0,-1.4],[0,0,0]])
var line2 = BEZIER(S0)([[0.8,-0.4,0],[0.8,0.2,2],[0.8,2.8,2],[0.8,2.8,-2],[0.8,0.2,-2],[0.8,-0.4,0]])
var line3 = BEZIER(S0)([[5.4,-2.4,0],[5.4,-2.4,3.2],[5.4,4.8,3.2],[5.4,4.8,-3.2],[5.4,-2.4,-3.2],[5.4,-2.4,0]])
var line4 = BEZIER(S0)([[10,-2.4,0],[10,-2.4,3.6],[10,5.2,3.6],[10,5.2,-3.6],[10,-2.4,-3.6],[10,-2.4,0]])
var line5= BEZIER(S0)([[14.55,-2.4,0],[14.55,-2.4,3.2],[14.55,5.1,3.2],[14.55,4.4,-3.2],[14.55,-2.4,-3.2],[14.55,-2.4,0]])
var line6= BEZIER(S0)([[14.8,-2.4,0],[14.8,-2.4,3.2],[14.8,4.4,3.2],[14.8,4.4,-3.2],[14.8,-2.4,-3.2],[14.8,-2.4,0]])
var line6bis= BEZIER(S0)([[15,-2.4,0],[15,-2.4,3.6],[15,6.8,3.6],[15,6.8,-3.6],[15,-2.4,-3.6],[15,-2.4,0]])
var line7 = BEZIER(S0)([[15.4,-2.4,0],[15.4,-2.4,5.6],[15.4,2.4,1.8],[15.4,10,0],[15.4,2.4,-1.8],[15.4,-2.4,-5.6],[15.4,-2.4,0]])
var line8 = BEZIER(S0)([[16,-2.4,0],[16,-2.4,3.2],[16,2.4,1.6],[16,8,0],[16,2.4,-1.6],[16,-2.4,-3.2],[16,-2.4,0]])
var line9 = BEZIER(S0)([[19.2,-2,0],[19.2,-2,3.2],[19.2,2.4,1.6],[19.2,4.8,0],[19.2,2.4,-1.6],[19.2,-2,-3.2],[19.2,-2,0]])
var line10 = BEZIER(S0)([[24,-1.8,0],[24,-1.8,2.8],[24,2.4,1.6],[24,3.2,0],[24,2.4,-1.6],[24,-1.8,-2.8],[24,-1.8,0]])
var line11 = BEZIER(S0)([[30-5.4,-1.4,0],[30-5.4,-1.4,1.6],[30-5.4,1.6,1.2],[30-5.4,1.2,0],[30-5.4,1.6,-1.2],[30-5.4,-1.4,-1.6],[30-5.4,-1.4,0]])
var line12 = BEZIER(S0)([[34.4-5.4,-0.4,0],[34.4-5.4,-0.4,0],[34.4-5.4,0.4,0.8],[34.4-5.4,0.4,0],[34.4-5.4,0.4,-0.8],[34.4-5.4,-0.4,-0],[34.4-5.4,-0.4,0]])
var line14=BEZIER(S0)([[37.4-5.4,-0.8,0],[37.4-5.4,-0.8,0],[37.4-5.4,0.8,1.2],[37.4-5.4,23.8,0],[37.4-5.4,0.8,-0.8],[37.4-5.4,-0.8,-1.2],[37.4-5.4,-0.8,0]])
var line15=BEZIER(S0)([[37.5-5.4,-0.8,0],[37.5-5.4,-0.8,0],[37.5-5.4,0.8,1.2],[37.5-5.4,23.8,0],[37.5-5.4,0.8,-0.8],[37.5-5.4,-0.8,-1.2],[37.5-5.4,-0.8,0]])
var line16=BEZIER(S0)([[37.6-5.4,-0.8,0],[37.6-5.4,-0.8,0],[37.6-5.4,0.8,1.2],[37.6-5.4,23.8,0],[37.6-5.4,0.8,-0.8],[37.6-5.4,-0.8,-1.2],[37.6-5.4,-0.8,0]])
var line17=BEZIER(S0)([[38-5.4,-0.8,0],[38-5.4,-0.8,0],[38-5.4,0.8,1.2],[38-5.4,7.8,0],[38-5.4,0.8,-0.8],[38-5.4,-0.8,-1.2],[38-5.4,-0.8,0]])
var line18=BEZIER(S0)([[38.2-5.4,-0.4,0],[38.2-5.4,-0.4,0],[38.2-5.4,0.8,1.2],[38.2-5.4,4.8,0],[38.2-5.4,0.8,-0.8],[38.2-5.4,-0.4,-1.2],[38.2-5.4,-0.4,0]])
var line19=[38.2-5.4,-0.4,0]


var fuselage1 = BEZIER(S1)([line1,line2,line3,line4])
var fuselage2 = BEZIER(S1)([line5,line6,line6bis,line7,line8,line9,line10,line11,line12,line14,line15,line16,line17,line18,line19])
var fuselage1 = MAP(fuselage1)(domain2d)
var fuselage2 = MAP(fuselage2)(domain2d)

var fuselage=STRUCT([fuselage1,fuselage2])
var fuselage = COLOR([0/255,49/255,83/255])(fuselage) 

//DRAW(fuselage)

//Punta

var tip = BEZIER(S1)([line13,line1])
tip =MAP(tip)(domain2d)
tip=COLOR([0])(tip)
//DRAW(tip)

//Vetro

var curvavetro1=BEZIER(S0)([[10.0,0,3.6],[10.0,3,3.6],[10.0,2.7,-3.6],[10.0,0,-3.6]])
var curvavetro2 = BEZIER(S0)([[11.2,0,3.7],[11.2,3,3.7],[11.2,3,-3.7],[11.2,-0,-3.7]])
var curvavetro3= BEZIER(S0)([[14.7,0,3.2],[14.7,2.9,3.2],[14.7,2.9,-3.85],[14.7,0,-3.2]])

var surfvetro = BEZIER(S1)([curvavetro1,curvavetro2,curvavetro3])
var surfacevetro = MAP(surfvetro)(domain2d)
var vetro = (surfacevetro)
vetro=SCALE([2])([0.55])(vetro)

fus=SCALE([1])([-1.1])(vetro)
fus=COLOR([0/255,49/255,83/255])(fus)
//DRAW(fus)


vetro=COLOR([168/255,207/255,241/255,0.85])(vetro)
//DRAW(vetro)



//Elica


var e1 = ([[0,0,0],[0,0.1,-0.3],[-0.2,0.5,-0.3]])
var e2= ([[-0.2,0.5,-0.3],[-0.1,1.9,-0.1]])
var e3=([[-0.1,1.9,-0.1] ,[-0.1,1.98,-0.1],[-0.1,2.0,0]])
e1=BEZIER(S0)(e1)
e2=BEZIER(S0)(e2)
e3=BEZIER(S0)(e3)

var e21 = ([[0,0,0],[0,0.1,0.3],[-0.2,0.5,0.3]])
var e22=([[-0.2,0.5,0.3],[-0.1,1.9,0.1]])
var e23=([[-0.1,1.9,0.1] ,[-0.1,1.98,0.1],[-0.1,2.0,0]])
e21=BEZIER(S0)(e21)
e22=BEZIER(S0)(e22)
e23=BEZIER(S0)(e23)

var s1 = BEZIER(S1)([e1,e21])
s1= MAP(s1)(domain2d)

var s2 = BEZIER(S1)([e2,e22])
s2= MAP(s2)(domain2d)

var s3 = BEZIER(S1)([e3,e23])
s3= MAP(s3)(domain2d)

var surface_elica=STRUCT([s1,s2,s3])
var elica= STRUCT(REPLICA(3)([surface_elica,R([1,2])(2*PI/(3))]))

elica = COLOR([0])(elica)
elica=SCALE([0,1,2])([0.8,0.8,0.8])(elica)
elica=T([0,1])([-2.3,0.8])(elica)

//DRAW(elica)


//bocchette

var c1 = CUBIC_HERMITE(S0)([[0,0.3,0.1],[0,0.3,-0.1],[1,0,0],[-1,0,0]])

var c2 = CUBIC_HERMITE(S0)([[0,0.3,0.1],[0,0.3,-0.1],[0,0,0],[0,0,0]])

var c3 = CUBIC_HERMITE(S0)([[0,0.3*2,0],[0,0.3*2,0],[0,0,0],[0,0,0]])

var vent = MAP(BEZIER(S1)([c1,c3,c2]))(domain2d)
vent = COLOR([0/255,49/255,83/255])(vent)
vent=R([1,2])([PI/2])(vent)
vent=T([0,1,2])([0,0,0.5])(vent)
var vent2 = S([2])([-1])(vent)
vent2=T([0,1,2])([-1.3,0,-0.18])(vent2)
vent = T([0,1,2])([-1.3,0,0.18])(vent)

var vents= STRUCT([vent, vent2])
vents = S([0])([-1])(vents)
vents=SCALE([0,1,2])([3.5,2,1.5])(vents)

vents=COLOR([0])(vents)
//DRAW(vents)


//ALI


var ali1 = BEZIER(S0)([[3.4,0.2,0.8*0.05],[0.4,0.4,0.8*0.05],[0.2,0.3,0.8*0.05],[0,0.6,0.9*0.05],[0,0.8,0.8*0.05],[0.7,0.8,0.8*0.05],[1.1,0.6,0.8*0.05],[2,0.6,0.8*0.05],[3.4,0.4,0+0.8*0.05]])
var ali2 = BEZIER(S0)([[3.7,2,0+2*0.05],[0.4,2,0+2*0.05],[0.2,2,0+2*0.05],[0,2,0.1+2*0.05],[0,2,0.4+2*0.05],[0.7,2,0.6+2*0.05],[1.1,2,0.6+2*0.05],[2,2,0.5+2*0.05],[3.7,2,0+2*0.05]])
var ali3 = BEZIER(S0)([[3.7,7,0+7*0.05],[0.4,7,0+7*0.05],[0.2,7,0+7*0.05],[0,7,0.1+7*0.05],[0,7,0.4+7*0.05],[0.7,7,0.6+7*0.05],[1.1,7,0.6+7*0.05],[2,7,0.5+7*0.05],[3.7,7,0+10*0.05]])
var ali4 = BEZIER(S0)([[3.7,8,0+8*0.05],[0.4,8,0+8*0.05],[0.2,8,0+8*0.05],[0,8,0.07+8*0.05],[0,8,0.3+8*0.05],[0.7,8,0.45+8*0.05],[1.1,8,0.45+8*0.05],[2,8,0.37+8*0.05],[3.7,8,0+8*0.05]])
var ali5 = BEZIER(S0)([[3.6,9,0+9*0.05],[1,9,0+9*0.05],[0.8,9,0+9*0.05],[0.6,9,0.05+9*0.05],[0.6,9,0.2+9*0.05],[1.3,9,0.3+9*0.05],[1.7,9,0.3+9*0.05],[2.4,9,0.25+9*0.05],[3.6,9,0+9*0.05]])
var ali7 = ([3.6,9.000001,9*0.05])

var ala = BEZIER(S1)([ali1,ali2,ali3,ali4,ali5,ali7])
ala = MAP(ala)(domain2d)
ala=R([1,2])(-PI/2)(ala)
ala=T([0,1,2])([5.7,-0.8,-0.68])(ala)
ala = COLOR([1,1,1])(ala)


var alabis = S([2])([-1])(ala)
alabis=T([2])([0.10])(alabis)

var ali = STRUCT([ala,alabis])
ali=SCALE([0,2])([2,1.4])(ali)

//DRAW(ali)

//alettoni

var alettone_1 = BEZIER(S0)([[3.4,0.8,0+0.8*0.05],[0.4,0.8,0+0.8*0.05],[0.2,0.8,0+0.8*0.05],[0,0,0.0+0.8*0.05],[0,0.8,0.+0.8*0.05],[0.7,0.8,0.+0.8*0.05],[1.1,0.8,0.+0.8*0.05],[2,0.8,0.+0.8*0.05],[3.4,0.8,0+0.8*0.05]])
var alettone_2 = BEZIER(S0)( [[3.7,2,0+2*0.05],[0.4,2,0+2*0.05],[0.2,2,0+2*0.05],[0,2,0.1+2*0.05],[0,2,0.4+2*0.05],[0.7,2,0.6+2*0.05],[1.1,2,0.6+2*0.05],[2,2,0.5+2*0.05],[3.7,2,0+2*0.05]])
var alettone_3 = BEZIER(S0)([[3.7,7,0+7*0.05],[0.4,7,0+7*0.05],[0.2,7,0+7*0.05],[0,7,0.1+7*0.05],[0,7,0.4+7*0.05],[0.7,7,0.6+7*0.05],[1.1,7,0.6+7*0.05],[2,7,0.5+7*0.05],[3.7,7,0+10*0.05]])
var alettone_4 = BEZIER(S0)([[3.7,8,0+8*0.05],[0.4,8,0+8*0.05],[0.2,8,0+8*0.05],[0,8,0.07+8*0.05],[0,8,0.3+8*0.05],[0.7,8,0.45+8*0.05],[1.1,8,0.45+8*0.05],[2,8,0.37+8*0.05],[3.7,8,0+8*0.05]])
var alettone_5 = BEZIER(S0)([[3.6,9,0+9*0.05],[1,9,0+9*0.05],[0.8,9,0+9*0.05],[0.6,9,0.05+9*0.05],[0.6,9,0.2+9*0.05],[1.3,9,0.3+9*0.05],[1.7,9,0.3+9*0.05],[2.4,9,0.25+9*0.05],[3.6,9,0+9*0.05]])
var alettone7 = ([3.6,9.000001,9*0.05])


var alettone = BEZIER(S1)([alettone_1,alettone_2,alettone_3,alettone_4,alettone_5,alettone7])
alettone = MAP(alettone)(domain2d)
alettone=R([1,2])(-PI/2)(alettone)
alettone=SCALE([0,1,2])([0.75,0.25,0.35])(alettone)
alettone=T([0,1,2])([29,2,-0.15])(alettone)

var alettonebis = S([2])([-1])(alettone)
alaettoneis=T([2])([0.1])(alettonebis)

var alettoni = STRUCT([alettone,alettonebis])

//DRAW(alettoni)









//ruote 

var domain = DOMAIN([[-PI/2,PI/2],[0,2*PI]])([12,24])

var torus = function (R, r) {
  return function (v) {
    var a = v[0]
    var b = v[1]

    var u = (r * COS(a) + R) * COS(b)
    var v = (r * COS(a) + R) * SIN(b)
    var w = (r * SIN(a))

    return [u,v,w]
  }
}

function annulus_sector (alpha, r, R) {
  var domain = DOMAIN([[0,alpha],[r,R]])([15,1])
  var mapping = function (v) {
    var a = v[0]
    var r = v[1]
    
    return [r*COS(a), r*SIN(a)]
  }
  var model = MAP(mapping)(domain)
  return model
}


var pneumatico = torus(3,1)
var pneumatico = MAP(pneumatico)(domain)

var pneumatico = COLOR([95/255,95/255,95/255])(pneumatico)


var cerchioneEsterno = annulus_sector(2*PI,2.8,3)
var cerchioneEsterno = EXTRUDE([2])(cerchioneEsterno)
var cerchioneEsterno = T([2])([-1])(cerchioneEsterno)
var cerchioneEsterno = COLOR([47/255, 47/255,47/255])(cerchioneEsterno)





var r = 0.5
var divs = 32
var circle = CIRCLE(r)(divs)
var cilinder=EXTRUDE([6])(circle)
cilinder=T([2])([-3])(cilinder)
cilindervertical= R([0,2])([-PI/2])(cilinder)
var tappo = DISK(0.5)(12)
tappo=T([2])([2.8+(1/2)-r/2])(tappo)
tappo=COLOR([0/255, 0/255,0/255])(tappo)
cilindervertical= T([2])([2.8-(r/2)])(cilindervertical)
cilindervertical= T([0])([2.8+(r)])(cilindervertical)
cilindervertical=COLOR([0/255, 0/255,0/255])(cilindervertical)
cilinder=COLOR([0/255, 0/255,0/255])(cilinder)

cilinderverticaldoppio=S([0])([1.5])(cilindervertical)

arm=STRUCT([cilinder,cilindervertical,tappo])
armbis=S([2])([-1])(arm)

arm2=STRUCT([cilinder,cilinderverticaldoppio,tappo])
armbis2=S([2])([-1])(arm2)


var cerchioneInterno = annulus_sector(2*PI,0.5,1)
var cerchioneInterno = EXTRUDE([2])(cerchioneInterno)
var cerchioneInterno = T([2])([-1])(cerchioneInterno)
var cerchioneInterno = COLOR([47/255, 47/255,47/255])(cerchioneInterno)


var raggio1 = SIMPLEX_GRID([[0.2],[-1,1.8],[2]])
var raggio1 = T([0,2])([-0.1,-1])(raggio1)
var raggio2 = R([0,1])([PI/4])(raggio1)
var raggio3 = R([0,1])([PI/4])(raggio2)
var raggio4 = R([0,1])([PI/4])(raggio3)
var raggio5 = R([0,1])([PI/4])(raggio4)
var raggio6 = R([0,1])([PI/4])(raggio5)
var raggio7 = R([0,1])([PI/4])(raggio6)
var raggio8 = R([0,1])([PI/4])(raggio7)

var raggi = STRUCT([raggio1, raggio2, raggio3, raggio4,raggio5,raggio6,raggio7,raggio8])
var raggi=COLOR([47/255, 47/255,47/255])(raggi)
var tot = STRUCT([pneumatico, raggi, cerchioneEsterno,cerchioneInterno])

var totR = SCALE([0,1,2])([0.25,0.25,0.25])(STRUCT([arm,armbis]))
var totR2 = SCALE([0,1,2])([0.25,0.25,0.25])(STRUCT([arm2,armbis2]))
tot = SCALE([0,1,2])([0.25,0.25,0.25])(tot)
totR=R([0,1])([-PI/2])(totR)
totR=R([0,1])([-PI])(totR)
tot=R([0,1])([-PI/2])(tot)
tot=R([0,1])([-PI])(tot)
totR2=R([0,1])([-PI/2])(totR2)
totR2=R([0,1])([-PI])(totR2)

totRbis=STRUCT([totR2,T([2])([9])(totR2)])
totbis=STRUCT([tot,T([2])([9])(tot)])
totRbis=T([0,1,2])([14.5,-3,-4.5])(totRbis)
totbis=T([0,1,2])([14.5,-3,-4.5])(totbis)

//DRAW(totRbis)

totR1=T([0,1])([4.5,-3.0])(totR)
tot1=T([0,1])([4.5,-3.0])(tot)
//tot1=S([1])([1.03])(tot1)
//DRAW(totR1)


function move() {
setInterval(function () {  
  totbis.rotate([0,1], PI/10) 
  tot1.rotate([0,1], PI/10)  
   elica.rotate([1,2],PI/5)      

       }, 60)

//DRAW(totbis)
//DRAW(tot1)
//DRAW(elica)
 
}
move()


//pista


var erba = COLOR([102/255,255/255,4/255])(SIMPLEX_GRID([[20],[-2.2, 0.5], [0.1]]))

var cemento = COLOR([47/255,47/255,47/255])(SIMPLEX_GRID([[20],[0.5, -0.1, 3, -0.1, 0.5],[0.1]]))


var erba1=T([0, 2])([-10, -1.1])(erba)
var erba2=T([0, 2, 1])([-10, -1.1, -4.7])(erba)

var cemento = T([2, 1, 0])([-1.1, -2, -10])(cemento)


var pista=STRUCT([erba1,cemento,erba2])
pista=R([1,2])([-PI/2])(pista)
pista=T([0,1,2])([-1,-2.92,0])(pista)
pista=SCALE([0,1,2])([18,1,15])(pista)




//questo sottostante è  il model con l'attivazione delle ruote e elica che girano,logiamente riattivando i DRAW all'interno della funzione move()

//var model =STRUCT([fuselage,tip,fus,vetro,vents,ali,alettoni,totRbis,totR1,pista])


var model =STRUCT([fuselage,tip,fus,vetro,vents,ali,alettoni,totRbis,totR1,elica,totbis,tot1,pista])
//DRAW(model)




  return model
  })();

  exports.author = 'matpresidentric';
  exports.category = 'vehicles';
  exports.scmodel = scmodel;

  if (!module.parent) {
    fs.writeFile('./data.json', JSON.stringify(scmodel.toJSON()));
  }

}(this));