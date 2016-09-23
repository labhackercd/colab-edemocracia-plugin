

// Quick proof of concept for search form toggle
// Would like to make CSS only

let searchWrapper = document.querySelector('.search-form'),
    searchInput = document.querySelector('.search-form__input');
    navBar = document.querySelector('.navigation');

document.addEventListener('click', (e) => {
  if (~e.target.className.indexOf('search-form')) {
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

window.getCookie = function(name) {
  match = document.cookie.match(new RegExp(name + '=([^;]+)'));
  if (match) return match[1];
}

// Set CSRF Token on ajax requests
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        }
    }
});

$('.category-list__button')
  .click(function() {
    $(this).toggleClass('active');
    $.post('/profile/update_prefered_theme/',
      {csrftoken: getCookie("csrftoken"),
       category_slug: $(this).attr('slug')}, null
    )
});

$('.c-hamburger')
  .click(function() {
    $(this).toggleClass('toggled');
    $('.navigation-wrapper').toggleClass('toggled');
});


// Input file name show 

(function($, window, document, undefined)
{
  $('.button--file-input').each( function()
  {
    var $input = $(this),
      $label = $input.next('label'),
      labelVal = $label.html();

    $input.on('change', function(e)
    {
      var fileName = '';

      if(this.files && this.files.length > 1)
        fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
      else if(e.target.value)
        fileName = e.target.value.split('\\').pop();

      if(fileName)
        $label.html(fileName);
      else
        $label.html(labelVal);
    });
  });
})(jQuery, window, document);

// User profile image input preview

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.user-profile--profile-page').attr('style','background-image:url("'+ e.target.result + '")');
        }
        reader.readAsDataURL(input.files[0]);
        $('.user-profile--profile-page i').hide();
    }
}

$(".user-figure__file-button").change(function(){
    readURL(this);
});
