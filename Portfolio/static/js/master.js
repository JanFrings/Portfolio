//////////////navbar links disappear on a certain path//////////////
// catching the html objects(acts simular to an array)
var index_navs = document.querySelectorAll('#IndexNav');
//  catching the url and spliting it by '/'(returns a list)
var url = window.location.pathname.split('/');

//////////////hidding particular navs in case a certain site is visited////////////////////////////////////////////////////
// checking the url elements for a match
for (var i = 0; i < url.length; i++) {
   if (url[i] == 'Projects' ||url[i] == 'signup' ||url[i] == 'login' ||url[i] == 'nfl') {
     // hidding the query html elements
     for (var k = 0; k < index_navs.length; k++) {
       index_navs[k].style.display='none';
     }
   }
}


//////////////navbar changes background and link color while scrolling past a certain point////////////////////////////////////////////
// adds classes as soon as the window scroll is below 750 //
setInterval(function(){
    if ($(window).scrollTop() >= 900) {
      $('nav').removeClass('scroll-up')
      $('nav').addClass('scroll-down')
      $('.nav-link').addClass('nav-link-black')

    }else if ($(window).scrollTop() <= 900) {
      $('nav').removeClass('scroll-down')
      $('nav').addClass('scroll-up')
      $('.nav-link').removeClass('nav-link-black')
    };
// check intervall in milliseconds
}, 250);


////////////// smooth scroll when using an anchor link in navbar/////////////////////////////////////////////////////////
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
