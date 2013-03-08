function fibonacci (n) {
  if (n===0){
	fibonacci[n]=0;
	}
else if ((n===1)||(n===2)){
	fibonacci[n]=1;
	}

else if (!(n in fibonacci)) {
    fibonacci[n] = fibonacci(n-2)+ fibonacci(n-1); 
  }

return fibonacci[n];
}
