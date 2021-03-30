$(document).ready(function() {

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var graph_received = [];
    

    socket.on('newTemperature', function(msg) {  
        $('#temp-log').html(msg.temperature.toString());
    })

    socket.on('newTime', function(msg) {
        $('#time-log').html(msg.time.toString());
    })

    socket.on('newGraph', function(msg) {
       
        if (graph_received.length >= 1) {
            graph_received.shift()
        }

        graph_received.push(msg.graph)
        img = '';         

        for (var i = 0; i < graph_received.length; i++) {
            img = graph_received[i].toString()
        } 

        $('#graph-log').html(img);
      
    
    })

    socket.on('newoutsideTemp', function(msg) {

        img = "<p>The Temperature Outside is : " + msg.outsideTemp.toString() + '&#176; C </p>'         
        $('#outside-log').html(img);  
    })


    socket.on('newOutsideFeelsLike', function(msg){

        outside = '<p> But outside it FEELS like : ' + msg.outsideFeelsLikeTemperature.toString() + '&#176; C </p>'
        $('#outside-feel-log').html(outside)
    })
   
})

