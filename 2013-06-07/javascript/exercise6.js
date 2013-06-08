//preso d'esempio da github...exercise dal examples.py del 2013-06-04
 


function convertion(v,fv) {
var lengthv = v.length;
var lengthfv=fv.length
v = model[0]
 fv = model[1]
 string = " "
 for (i=0; i<length;i++){string =string+ "v "+v[i][0] +" " + v[i][1] +" " +0 + "\n" }

        string =string+ "\n\n#########:\n";

            for (i=0; i<lengthfv;i++){
       string =string+ "  "
 	

 	for (j=0; j<fv[i].length;j++)
	 	string=string+ fv[i][j] +" "
 string =string+ "\n"
 }
 return string;
}









FV = [[5,6,7,8],[0,5,8],[0,4,5],[1,2,4,5],[2,3,5,6],[0,8,7], [3,6,7], [1,2,3], [0,1,4]]

V = [[0,6],[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[6,6],[3,6]]

lar = [V,FV]





var convert = convertion(lar);