var domain = INTERVALS(1)(32)
var domain2D = PROD1x1([INTERVALS(1)(32),INTERVALS(1)(32)])




var m =[]
var mb =[]

for(i=0;i<10;i++){
  var a=new Array()
  var b=new Array()
  for(j=0;j<10;j++){
   var r=Math.random()
  if((r*10)%5>2.5)r1=3+r
  else if((r*10)%5==0)r1=-4*r
      else r1=r*3
   a.push((r1));
 b.push(r)
}
m.push(a)
mb.push(b)
}

var curve = []


   
  for (i=0;i < 10;i++ ) {
     var p1 = []
     var p2 = []
     var p3 = []
     var p4 = []
     var p5 = []
     var p6 = []
     var p7 = []
     var p8 = []
     var p9 = []
     var p10 =[] 
     
     
     for(j=0 ;j<10 ;j++){    
      if(j===0){       
       p1.push(j)
       p1.push(i)
       p1.push(m[i][j])     
      }
      if(j===1){       
       p2.push(j)
       p2.push(i)
       p2.push(m[i][j])     
      }
      if(j===2){       
       p3.push(j)
       p3.push(i)
       p3.push(m[i][j])          
        }
        if(j===3){       
       p4.push(j)
       p4.push(i)
       p4.push(m[i][j])          
        }
        if(j===4){       
       p5.push(j)
       p5.push(i)
       p5.push(m[i][j])          
        }
        if(j===5){       
       p6.push(j)
       p6.push(i)
       p6.push(m[i][j])          
        }
        if(j===6){       
       p7.push(j)
       p7.push(i)
       p7.push(m[i][j])          
        }
        if(j===7){       
       p8.push(j)
       p8.push(i)
       p8.push(m[i][j])          
        }
        if(j===8){       
       p9.push(j)
       p9.push(i)
       p9.push(m[i][j])          
        }
        if(j===9){       
       p10.push(j)
       p10.push(i)
       p10.push(m[i][j])           
        }
        
     }
     
     var line =[]
     line.push(p1)
     line.push(p2)
     line.push(p3)
     line.push(p4)
     line.push(p5)
     line.push(p6)
     line.push(p7)
     line.push(p8)
     line.push(p9)
     line.push(p10)
    
     var curva= BEZIER(S0)(line)
     curve.push(curva)     
  
  }



var s = BEZIER(S1)([curve[0],curve[1],curve[2],curve[3],curve[4],curve[5],curve[6],curve[7],curve[8],curve[9]])
s = MAP(s)(domain2D)
s = COLOR(([122/255,84/255,59/255]))(s)
s=T([2])([-2])(s)
//DRAW(s)



//lake

var l = COLOR(([0,255/255,178/255]))(CUBOID([9,9,0.2]))
//var l = T([0,1,2])([3.4,6.8,-0.2])(l)
var tl = STRUCT([s,l])
DRAW(tl)


/*for(i=0;i<10;i++)
  for(j=0;j<10;j++){
   if(m[i][j]<0) DRAW(T([0,1])([i,j])(l))

}
*/

var r=0.1
var circle = CIRCLE(r)(32)
var cilinder=EXTRUDE([1])(circle)
var domain = DOMAIN([[0,1],[0,2*PI]])([20,20])
var profile = BEZIER(S0)([[-0.3,0.3,-0.6],[0,0,0]])
var mapping = ROTATIONAL_SURFACE(profile)
var surface = MAP(mapping)(domain)
var surface=T([2])([1.3])(surface)
var albero=STRUCT([COLOR(([34/255,139/255,34/255]))(surface),COLOR(([92/255,51/255,23/255]))(cilinder)])
albero=S([0,1,2])([0.5,0.5,0.5])(albero)
//DRAW(albero)


var alberi;
for(i=0;i<10;i++){
  for(j=0;j<10;j++){
    var ap=m[i][j];
     var ap1=mb[i][j]
    if((ap>3.3) && (ap<=3.5)){
      alberoapp=T([0,1,2])([i+0.1,j+0.1,ap1])(albero)
      alberi=STRUCT([alberoapp,alberi])

    }
}
}
DRAW(alberi)
/*var albero1=T([0,1,2])([8,7,0.])(albero)
var albero2=T([0,1,2])([8,8.5,0.3])(albero)
var albero3=T([0,1,2])([3,6,0.7])(albero)
var albero4=T([0,1,2])([0.1,7,0])(albero)
var albero5=T([0,1,2])([0.2,8,0.2])(albero)

var alberi=STRUCT([albero1,albero2,albero3,albero4,albero5])
DRAW(alberi)*/