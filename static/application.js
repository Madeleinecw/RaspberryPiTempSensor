$(document).ready(function() {

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var temperature_received = [];
    var time_received = [];
    var graph_received = [];
    var outside_received = [];
    

    socket.on('newTemperature', function(msg) {
        
        if (temperature_received.length >= 1) {
            temperature_received.shift()
        }

        temperature_received.push(msg.temperature)
        temperatures_string = '  ';

        for (var i = 0; i < temperature_received.length; i++) {
            temperatures_string = temperatures_string + temperature_received[i].toString();
        }
        $('#temp-log').html(temperatures_string);
    })

    socket.on('newTime', function(msg) {

        if (time_received.length >= 1) {
            time_received.shift()
        }

        time_received.push(msg.time)
        time_string = '  ';

        for (var i = 0; i < time_received.length; i++) {
            time_string = time_string +  time_received[i].toString();
        }
        $('#time-log').html(time_string);
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
       
        console.log(msg.outsideTemp)

        if (outside_received.length >= 1) {
            outside_received.shift()
        }
        
        outside_received.push(msg.outsideTemp)
        img = '';         
        
        for (var i = 0; i < outside_received.length; i++) {
            img = "<p>The Temperature Outside is :" + outside_received[i].toString() + '&#176; C </p>'
        }
        

        $('#outside-log').html(img);
      
    
    })
 
})

