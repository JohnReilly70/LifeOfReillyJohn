

$(document).ready(function(){

    var scrollLink = $('.nav-link');

    scrollLink.click(function(e) {
    e.preventDefault();
    $('body,html').animate({
      scrollTop: $(this.hash).offset().top -100
    }, 1000 );
  });


    $(window).scroll(function(){
        var scrollbarLocation = $(this).scrollTop();
        console.log(scrollbarLocation);
            scrollLink.each(function() {

      var sectionOffset = $(this.hash).offset().top - 400;

      if ( sectionOffset <= scrollbarLocation ) {

        $(this).addClass('active');
        $(this).siblings().removeClass('active');
      }

       if ( scrollbarLocation < 150) {

        $( 'div .navbar-nav' ).find( 'a.active' ).removeClass( 'active' );
      }

    })

    });

});


