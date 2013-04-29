function esercizio(n){
  var array=[];
  for (var i = 0; i < n; i++) {
  	array[i]=i;
  };
 console.log("ARRAY INIZIALE : "+array);
var risultato=array.filter(function(item){
	return (item % 2===0);
})
.map(function(item){
	return item*2;
})
.filter(function(item){
 return (item % 4=== 0);
})
.reduce(function(prev, cur){
 return prev + cur;
});

console.log(risultato);


}