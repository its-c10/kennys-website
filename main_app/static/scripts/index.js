$(document).ready(function () {
    $("#nav-bars-wrapper").click(function () {
        $("#side-nav").toggleClass('show');
    });

});

$(function () {

    $(document).scroll(function () {

        let $nav = $(".main-nav");
        let $linksInNav = $(".main-nav a");

        var shouldTurnNavWhite = $(this).scrollTop() > $nav.height();

        $nav.toggleClass('scrolled', shouldTurnNavWhite);
        $linksInNav.toggleClass('toggleLinkColor', shouldTurnNavWhite);

        var navBars = $("#nav-bars");
        if (shouldTurnNavWhite) {
            navBars.css("color", "black");
        } else {
            navBars.css("color", "white");
        }

        var jumbo = $("#jumbo");
        var sideNav = $("#side-nav");
        var sideNavLinks = $("#side-nav a");
        var shouldTurnNavWhite = sideNav.offset().top > jumbo.height();
        if (shouldTurnNavWhite) {
            sideNav.css("background-color", "black");
            sideNavLinks.css("color", "white");
            sideNav.css("border-color", "white");
        } else {
            sideNav.css("background-color", "white");
            sideNavLinks.css("color", "black");
            sideNav.css("border-color", "black");
        }

    });

});


