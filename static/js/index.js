function cleanForm() {
    document.getElementById('url').value = '';
    var keywordsContainer = document.querySelector('.keywords-container-horizontal');
    if (keywordsContainer) {
        keywordsContainer.innerHTML = '';
    }

    var keywordsContainer = document.querySelector('.keywords-container');
            if (keywordsContainer) {
                keywordsContainer.innerHTML = '';
            }
}