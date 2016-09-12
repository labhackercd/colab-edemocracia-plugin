$(document).foundation();

// Quick proof of concept for search form toggle
// Would like to make CSS only

let searchWrapper = document.querySelector('.search-form'),
    searchInput = document.querySelector('.search-form__input');
    navBar = document.querySelector('.navigation');

document.addEventListener('click', (e) => {
  if (~e.target.className.indexOf('search')) {
    searchWrapper.classList.add('focused');
    navBar.classList.add('search-on');
    searchInput.focus();
  } else {
    searchWrapper.classList.remove('focused');
    navBar.classList.remove('search-on');
  }
});

$('.menu-list--dropdown')
  .click(function() {    
    $('.menu-list--dropdown, .menu-list--dropdown__wrapper')
      .not(this)
      .removeClass('toggled');

    $(this)
      .toggleClass('toggled');

    $(this)
      .find('.menu-list--dropdown__wrapper')
      .addClass('toggled');
});

$('.menu-list--dropdown__wrapper')
  .click(function() { 
    event.stopPropagation();
});

$(document).click(function(e) { 
    var target = e.target
    if (!$(target).closest('.toggled').length) {
      
      $('.toggled')
        .removeClass('toggled');
    }  
});

$('.login-box__option')
  .click(function() {  
    var selectedOption = $(this);

    if (!selectedOption.hasClass('active')) { 

      $('.login-box__form-wrapper.active')
        .addClass('transition')
        .bind('transitionend MSTransitionEnd webkitTransitionEnd oTransitionEnd', function() {

          $('.login-box__form-wrapper')
            .toggleClass('active')
            .toggleClass('inactive');

          $('.login-box__form-wrapper')
          .unbind()
          .removeClass('transition');

        });

      $('.login-box__yellow-bar')
        .addClass('active')
        .bind('transitionend MSTransitionEnd webkitTransitionEnd oTransitionEnd', function() {

          $('.login-box__option')
            .removeClass('active');

          selectedOption
            .addClass('active');

          $('.login-box__yellow-bar')
            .unbind()
            .removeClass('active');
      });
    }  
});

$('.category-list__button')
  .click(function() {  
    $(this).toggleClass('active');
});  

$('.c-hamburger')
  .click(function() {  
    $(this).toggleClass('toggled');
    $('.navigation-wrapper').toggleClass('toggled');
});