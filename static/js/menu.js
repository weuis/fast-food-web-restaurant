document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const menuItems = document.querySelectorAll('.menu-item');

    searchInput.addEventListener('input', function () {
        let searchValue = this.value.toLowerCase();

        menuItems.forEach(function (item) {
            let itemName = item.getAttribute('data-name');

            if (itemName.includes(searchValue)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
});
