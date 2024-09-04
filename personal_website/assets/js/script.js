let slideIndex = 0;
imgCarousel();

function imgCarousel() {
    let slides = document.getElementsByClassName("page6-1carousel")[0].getElementsByTagName("img");
    
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.opacity = "0";
    }

    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.opacity = "1";
    
    setTimeout(imgCarousel, 2000);
}
