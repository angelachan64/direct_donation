//console.log("hi");

function getEmails() {
    var oTable = document.getElementById('paypal-stats');
    var l = [];
    for (var i = 0; i < oTable.rows.length; i++) {
	if (i != 0) {
	    var oCells = oTable.rows.item(i).cells;
	    EMAILCOL=8;
	    var cellVal = oCells.item(EMAILCOL).innerHTML;
	    console.log(cellVal);
	    l.push(cellVal);
	}
    }
    
    var target = document.getElementById("emails-list");
    target.innerHTML = l;
}

document.getElementById("emails-button").addEventListener("click",getEmails);

//console.log("bye");
