window.onload = function () {

    var slider = document.getElementById("car-quantity-range");
    var output = document.getElementById("car-quantity-value");

    output.innerHTML = slider.value;

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;
    }

    var serviceTypeSelect = document.getElementById("service-selection");

    serviceTypeSelect.oninput = function () {
        var value = this.value;
        var otherServiceInput = document.getElementById("service-selection-other-input");
        if (value == "service-other") {
            otherServiceInput.style.display = "block";
        } else {
            otherServiceInput.style.display = "none";
        }
    }

}
