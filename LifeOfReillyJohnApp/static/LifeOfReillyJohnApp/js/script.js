$(document).ready(function() {

    if (window.location.pathname != '/') {
        // Index (home) page
        return;
    }

    var scrollLink = $('.nav-link-scroll');

    scrollLink.click(function(e) {
        e.preventDefault();
        $('body,html').animate({
            scrollTop: $(this.hash).offset().top - 100
        }, 1000);
    });


    $(window).scroll(function() {
        var scrollbarLocation = $(this).scrollTop();
        scrollLink.each(function() {

            var sectionOffset = $(this.hash).offset().top - 400;

            if (sectionOffset <= scrollbarLocation) {
                $('div .navbar-nav').find('a.active').removeClass('active');
                $(this).addClass('active');
            }

            if (scrollbarLocation < 150) {

                $('div .navbar-nav').find('a.active').removeClass('active');
            }

        })

    });



});