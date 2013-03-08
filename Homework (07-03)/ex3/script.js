var x='\n';
var n = 10;
var m = 10;
for (var i = 0; i < n; i++) {
 for (var j = 0; j < m; j++) {

if((j)===(i))x+=1;
   else x+=0;

if((j+1)!==10){x +=',';}

  x +='\t'
  }
x += '\n';
}
console.log(x)
