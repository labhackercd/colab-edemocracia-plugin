$(document).foundation();

// Quick proof of concept for search form toggle
// Would like to make CSS only

let searchWrapper = document.querySelector('.search-form'),
    searchInput = document.querySelector('.search-form__input');

document.addEventListener('click', (e) => {
  if (~e.target.className.indexOf('search')) {
    searchWrapper.classList.add('focused');
    searchInput.focus();
  } else {
    searchWrapper.classList.remove('focused');
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

