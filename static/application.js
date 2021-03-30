$(document).ready(function() {

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var time_received = [];
    var graph_received = [];
    

    socket.on('newTemperature', function(msg) {
        
   
        $('#temp-log').html(msg.temperature.toString());
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

        img = "<p>The Temperature Outside is : " + msg.outsideTemp.toString() + '&#176; C </p>'         
        

        $('#outside-log').html(img);
      
    
    })
 
})

