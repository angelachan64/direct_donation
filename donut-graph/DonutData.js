var salesData=[
    {label:"Basic", color:"#3366CC", value: 133},
    {label:"Plus", color:"#DC3912", value: 213},
    {label:"Lite", color:"#FF9900", value: 123},
    {label:"Elite", color:"#109618", value: 200},
    {label:"Delux", color:"#990099", value: 100}
];

var svg = d3.select("body").append("svg").attr("width",700).attr("height",300);
svg.append("g").attr("id","salesDonut");

Donut3D.draw("salesDonut", randomData(), 150, 150, 130, 100, 30, 0.4);

function randomData(){
    return salesData.map(function(d){ 
	return {label:d.label, value:d.value, color:d.color};});
}

