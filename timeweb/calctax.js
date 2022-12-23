function calcTax(price, per) {
    alert(price + price * per / 100);
}

function tax(){
    var nedan1 = document.getElementById("nedan").value;
    var zeiritu1 = document.getElementById("zeiritu").value;
    var result =  parseInt(nedan1, 10) * (100 + parseInt(zeiritu1, 10)) / 100;
    var result1 = Math.floor(result);
    
    alert(result1);
  }