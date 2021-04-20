$(document).ready(function() {
    $("#owl-demo").owlCarousel({
        navigation: true,
        slideSpeed: 600,
        paginationSpeed: 500,
        singleItem: true,
        autoPlay: true,
        stopOnHover: true,
        navigationText: ["", ""],
        transitionStyle: "fade",
    });
    $("#owl-demo1").owlCarousel({
        navigation: true,
        navigationText: ["", ""],
        autoPlay: 3000,
        items: 3,
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [979, 1],
        stopOnHover: true,
        autoHeight: true,
    });
    $("#owl-demo2").owlCarousel({
        navigation: true,
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        autoPlay: 3000,
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [979, 1],
        stopOnHover: true,
        autoHeight: true,
    });
    $("#owl-demo3").owlCarousel({
        navigation: true,
        navigationText: ["", ""],
        autoPlay: 3000,
        items: 4,
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [979, 1],
        stopOnHover: true,
        autoHeight: true,
    });
});