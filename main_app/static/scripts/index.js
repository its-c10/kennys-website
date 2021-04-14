$(function () {
    $(document).scroll(function () {

        //let $leftSideJumbo = $("#left-side-jumbo-wrap");

        let $nav = $("#nav");
        let $linksInNav = $("#nav a");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
        $linksInNav.toggleClass('toggleLinkColor', $(this).scrollTop() > $nav.height());

        //let $getStartedBtn = $("#nav-get-started");
        //$getStartedBtn.toggleClass('displayed', ($(this).scrollTop() - 150) > $leftSideJumbo.height());

    });
});