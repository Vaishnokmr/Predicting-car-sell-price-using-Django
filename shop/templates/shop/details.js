var entry = document.getElementById("entry");
entry.addEventListener('click',displayDetails);

var row = 1;

function displayDetails(){

    var Present_Price = document.getElementById("Present_Price").values;
    var Kms_Driven = document.getElementById("Kms_Driven").values;
    var Owner = document.getElementById("Owner").values;
    var Old_Car = document.getElementById("Old_Car").values;
    var fuel = document.getElementById("fuel").values;
    var Seller_Type_Individual = document.getElementById("Seller_Type_Individual").values;
    var Transmission_Manual = document.getElementById("Transmission_Manual").values; 

    if(!Present_Price || !Kms_Driven || !Owner || !Old_Car || !fuel || !Seller_Type_Individual || !Transmission_Manual ) {

        alert("Please fill the details")
        return;
    }

    var display = document.getElementById("display");
    var newRow = display.insertRow(row);
    var cell1 = newRow.insertCell(0)
    var cell2 = newRow.insertCell(1)

    



}
    
    
    
    
    
   