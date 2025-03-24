// Drop Down
document.addEventListener("DOMContentLoaded", function() {
    let dropdowns = document.querySelectorAll(".dropdown > a");

    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default link behavior
            let menu = this.nextElementSibling;
            menu.style.display = menu.style.display === "block" ? "none" : "block";
        });
    });
});




// blog carousel
document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel-container");
    const items = document.querySelectorAll(".carousel-item");
    let index = 0;
    let itemWidth = items[0].offsetWidth;

    // Clone first few items for smooth infinite effect
    items.forEach(item => {
        let clone = item.cloneNode(true);
        carousel.appendChild(clone);
    });

    function updateWidth() {
        itemWidth = items[0].offsetWidth;
    }

    function moveCarousel() {
        index++;
        const offset = index * itemWidth;
        carousel.style.transition = "transform 0.5s ease-in-out";
        carousel.style.transform = `translateX(-${offset}px)`;

        if (index >= items.length / 2) {
            setTimeout(() => {
                carousel.style.transition = "none";
                carousel.style.transform = `translateX(0px)`;
                index = 0;
            }, 500);
        }
    }

    setInterval(moveCarousel, 3000);
    window.addEventListener("resize", updateWidth);
});


// about header

        // Add subtle parallax effect on mouse movement
        document.addEventListener("mousemove", (e) => {
            const imageContainer = document.querySelector(".image-container");
            const xAxis = (window.innerWidth / 2 - e.pageX) / 50;
            const yAxis = (window.innerHeight / 2 - e.pageY) / 50;
          
            imageContainer.style.transform = `translateX(${xAxis}px) translateY(${yAxis}px)`;
          });
          
          // Add fade-in animation on page load
          document.addEventListener("DOMContentLoaded", () => {
            const content = document.querySelector(".content");
            const imageContainer = document.querySelector(".image-container");
          
            // Set initial opacity
            content.style.opacity = "0";
            imageContainer.style.opacity = "0";
          
            // Add transition property
            content.style.transition = "opacity 1.5s ease";
            imageContainer.style.transition = "opacity 2s ease";
          
            // Trigger animation after a short delay
            setTimeout(() => {
              content.style.opacity = "1";
              imageContainer.style.opacity = "0.9";
            }, 300);
          });


    //  Team
    document.addEventListener("DOMContentLoaded", function() {
        let teamMembers = document.querySelectorAll(".team-member");
        let observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        }, { threshold: 0.2 });

        teamMembers.forEach(member => {
            observer.observe(member);
        });
    });
          