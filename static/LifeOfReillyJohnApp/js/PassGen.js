$(document).ready(function(){
    $('#PassGen').click(function() {

        var pass_len = $("#characters").val();
        var numbers = $("#numbers").val();
        var special = $("#special").val();
        var both = parseInt(numbers)+parseInt(special);

        if ((numbers > pass_len) || (special > pass_len) || (both  > pass_len) ){
            $("#Password").text("Password Length Must Be Greater Than Or Equal To Numbers & Special Characters Combined");
        } else {

        alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
        number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        var special_array = ['!','£','$','%','^',"&", "*", "#"];


        var password = [];


        for (var i = 0; i < numbers; i++) {
          password.push(number_array[Math.floor(Math.random() * number_array.length)])
        };

        for (var i = 0; i < special; i++) {
          password.push(special_array[Math.floor(Math.random() * special_array.length)])
        };


        for (var i = 0; i < (pass_len - numbers - special); i++) {
          password.push(alphabet_array[Math.floor(Math.random() * alphabet_array.length)])
        };


          function shuffle(a) {
            var j, x, i;
            for (i = a.length - 1; i > 0; i--) {
                j = Math.floor(Math.random() * (i + 1));
                x = a[i];
                a[i] = a[j];
                a[j] = x;
            }
            return a;
        }

        $("#Password").text(shuffle(password).join(""));
        }


    });

});


