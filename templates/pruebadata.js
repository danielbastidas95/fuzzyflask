


$(document).ready(function(){

    $.ajax({
        url:'datamain.csv',
        dataType: 'text',
        contentType:'charset=utf-8',
    }).done(changecolor);
    
    function changecolor(data){
        var datos = data.split(/\r?\n|\r/);
        datos = data.split(' ');
        datos = data.split('\r\r\n');
        
        var obj1 = datos[1].split(',')
        var valor_obj1 = obj1[1];
        valor_obj1 = parseInt(valor_obj1);

        
        document.getElementById("ini_1_1").style.background = "brown";
        document.getElementById("value_1_1").innerHTML = valor_obj1 + "%";
    }
})