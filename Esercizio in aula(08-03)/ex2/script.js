function esercizio(n){
  var array=[];
  for (var i = 0; i < n; i++) {
  	array[i]=Math.ceil(Math.random()*1000);
  };
 console.log("ARRAY INIZIALE : "+array);
var risultato=array.filter(function(item){
	return (item % 2===0);
});
console.log(risultato);
var compare = function (value1, value2) {
 return value1 - value2;
};
risultato.sort(compare);
console.log(risultato);
}