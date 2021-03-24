$(document).ready(function() {

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var temperature_received = [];
    var time_received = [];
    var graph_received = [];

    socket.on('newTemperature', function(msg) {
        console.log('The Temperature is ' + msg.temperature)
        
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
        console.log('The Time is ' + msg.time)

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
        console.log('The Graph has updated' + msg.graph)

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
})