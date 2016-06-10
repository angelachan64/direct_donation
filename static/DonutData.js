function getMoneys() {
    var oTable = document.getElementById('paypal-stats');
    var l = [];
    for (var i = 0; i < oTable.rows.length; i++) {
	if (i != 0) {
	    var oCells = oTable.rows.item(i).cells;
	    MONEYCOL=5;
	    var cellVal = oCells.item(MONEYCOL).innerHTML;
	    //console.log(cellVal);
	    l.push(cellVal);
	}
    }
    return l;
}    


function getFullNames() {
    var oTable = document.getElementById('paypal-stats');
    var l = [];
    for (var i = 0; i < oTable.rows.length; i++) {
	if (i != 0) {
	    var oCells = oTable.rows.item(i).cells;
	    FNAMECOL=0;
	    var cellVal1 = oCells.item(FNAMECOL).innerHTML;
	    LNAMECOL=1;
	    var cellVal2 = oCells.item(LNAMECOL).innerHTML;
	    //console.log(cellVal);
	    l.push(cellVal1 + cellVal2);
	}
    }
    return l
}    



var salesData=[];
var moneys = getMoneys();
var names = getFullNames();
for (var i = 0; i < moneys.length; i++) {
    salesData.push(
	{label: names[i], color: "#3366CC", value: moneys[i]}
    )
}
console.log(salesData);


// var salesData=[
//     {label:"Basic", color:"#3366CC", value: 133},
//     {label:"Plus", color:"#DC3912", value: 213},
//     {label:"Lite", color:"#FF9900", value: 123},
//     {label:"Elite", color:"#109618", value: 200},
//     {label:"Delux", color:"#990099", value: 100}
// ];

var svg = d3.select("body").append("svg").attr("width",700).attr("height",300);
svg.append("g").attr("id","salesDonut");

/////////////////////////////////////////////////////////////
// UNCOMMENT THIS TO MAKE THE DONUT GET DRAWN - DO IT! :)) //
/////////////////////////////////////////////////////////////
// Donut3D.draw("salesDonut", randomData(), 150, 150, 130, 100, 30, 0.4);

function randomData(){
    return salesData.map(function(d){ 
	return {label:d.label, value:d.value, color:d.color};});
}
