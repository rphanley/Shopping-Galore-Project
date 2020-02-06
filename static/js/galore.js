var orderFields = {
	id_full_name : null,
	id_phone_number : null,
	id_country : null,
	id_postcode : null,
	id_town_or_city : null,
	id_street_address1 : null,
	id_street_address2 : null,
	id_county : null

};

let data_saved = localStorage.getItem("data_saved");
if (data_saved === Boolean(true).toString()) {
	orderFields = JSON.parse(localStorage.getItem("form_data"));
}


function storeFormField() {
if (event.srcElement.value !== "") {
orderFields[event.srcElement.id]=event.srcElement.value;
localStorage.setItem("form_data", JSON.stringify(orderFields) );
localStorage.setItem("data_saved", "true");
console.log("Storing field..done");
}
else {
    console.log("Not storing blank field..");
}


}

function clearStorage() {

	if (data_saved === Boolean(true).toString()) {
		console.log("Clearing form data on Submit..");
		localStorage.removeItem("form_data");
		localStorage.setItem("data_saved", "false");
	}
}



function onFormLoad() {
console.log("Order form loaded..");
 
    if (data_saved === Boolean(true).toString()) {
	if (confirm("There is saved name/address data available. Click OK to use it in the form, or Cancel to continue with a blank form.")) {   
		
		for (var key in orderFields){
    			    			
    			console.log(key, orderFields[key]);
		 document.getElementById(key).value = orderFields[key];
			
		}

	}
	else {
		localStorage.removeItem("form_data");
		localStorage.setItem("data_saved", "false");
		console.log("form_data removed from local storage..");
	}

        
    }


}


$("#orderForm").one("click", onFormLoad);
