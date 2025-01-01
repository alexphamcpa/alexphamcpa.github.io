function openTab(tabName) {
    const contents = document.querySelectorAll('.tab-content');
    const links = document.querySelectorAll('.tab-link');
    contents.forEach(content => content.classList.remove('active'));
    links.forEach(link => link.classList.remove('active'));
    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');
}