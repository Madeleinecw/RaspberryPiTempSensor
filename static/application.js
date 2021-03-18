$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('my response', function(msg) {
        $('#log').append('<p>Received:' + msg.data + '</p>');
    });
    $('form#emit').submit(function(event){
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
});