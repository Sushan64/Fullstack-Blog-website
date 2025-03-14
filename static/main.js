// Mobile menu toggle functionality
    document.getElementById('menu-toggle').addEventListener('click', function() {
      const mobileMenu = document.getElementById('mobile-menu');
      mobileMenu.classList.toggle('hidden');
    });

// Spinner
document.getElementById("loadMoreLink").addEventListener("click", function(event) {
        let spinner = document.getElementById("spinner");
        spinner.classList.remove("hidden");
    });