let x ="global";
if(true){
   //TDZ for block-scoped "X " starts here  
   //console.log(x); // This would cause a ReferenceError
            //()NOTE: not global x but block-scoped x is in TDZ until it is declared and initialized 

      let x = "block";    
  console.log(x);
}
