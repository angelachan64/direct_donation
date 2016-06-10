var colArray = $('#paypal-stats td:nth-child(3)').map(function(){
    return $(this).text();
}).get()​;

console.log(colArray)

