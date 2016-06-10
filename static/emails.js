//console.log("hi");


var oTable = document.getElementById('paypal-stats');
//console.log("oTable:");
//console.log(oTable);

// var rowLength = oTable.rows.length;
// for (i = 0; i < rowLength; i++){
//     var oCells = oTable.rows.item(i).cells;
//     var cellLength = oCells.length;
//     // for(var j = 0; j < cellLength; j++){
//     //     var cellVal = oCells.item(j).innerHTML;
//     //     console.log(cellVal);
//     // }
//     for(var j = 0; j < cellLength; j++){
// 	var cellVal = oCells.item(j).innerHTML;
// 	console.log(cellVal);
//     }
// }

for (var i = 0; i < oTable.rows.length; i++) {
    var oCells = oTable.rows.item(i).cells;
    //for (var j = 0; j < oCells.length; j++) {
    EMAILCOL=8;
    j=EMAILCOL;
	var cellVal = oCells.item(j).innerHTML;
	console.log(cellVal);
    //}
}

//console.log("bye");
