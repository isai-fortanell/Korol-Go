btn = document.getElementById('hbger_btn')
li = document.getElementById('hbger_li')
nav = document.getElementsByClassName('buttons_navbar_inner')[0];
nav.classList.toggle('inactive')
li.classList.toggle('active')
btn_clicked = false;

btn.addEventListener('click', () => {
    nav.className =  'buttons_navbar_inner active'
    li.classList.toggle('active')
    btn.innerText = ">";
    if (btn_clicked == false) {
        btn_clicked = true;
        btn.innerText = ">";
    } else {
        nav.className =  'buttons_navbar_inner inactivating'
        btn_clicked = false;
        btn.innerText = "☰";
    }

})