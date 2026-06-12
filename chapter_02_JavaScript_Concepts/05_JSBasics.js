function letExample2(){
 let x = 10;
 
 if(true){
 let x = 30; //block scope 
 // y=13;
console.log(x);
//console.log(y) 
    
}
else
console.log(x =20);

}

letExample2()