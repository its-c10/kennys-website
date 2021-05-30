function openModal(serviceType, price, description) {

    setTimeout(function () {
        var $modal = $("#services-modal");
        if (!$modal.hasClass('show')) {
            $modal.toggleClass('show');
        }

        $("#services-modal h2").text(serviceType);
        $("#services-modal div p").text(description);
    }, 10);

}

window.addEventListener('click', function (e) {
    var servicesModal = document.getElementById('services-modal');
    if (!servicesModal.contains(e.target) && servicesModal.classList.contains('show') && e.target.tagName != 'A') {
        $("#services-modal").toggleClass('show');
    }
});