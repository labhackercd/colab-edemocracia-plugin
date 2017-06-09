// Quick proof of concept for search form toggle
// Would like to make CSS only

var searchWrapper = $('.search-form');
var searchInput = $('.search-form__input');
    navBar = $('.navigation');

$(document).click(function(e){
  if (~e.target.className.indexOf('search-form')) {
    $(searchWrapper).addClass('focused');
    $(navBar).addClass('search-on');
    searchInput.focus();
  } else {
    $(searchWrapper).removeClass('focused');
    $(navBar).removeClass('search-on');
  }
});

// Hide nav on scroll

// grab an element
var myElement = document.querySelector('body');
// construct an instance of Headroom, passing the element
var headroom  = new Headroom(myElement, {
  "tolerance" : {
        up : 15,
        down : 0
    }
});
// initialise
headroom.init();
$('body').addClass('headroom--pinned');

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

$('.show-filters')
  .click(function() {
    $(this).toggleClass('active');
    $('.section--filter-select').slideToggle();
    return false;
})

$('.c-hamburger')
  .click(function() {
    $(this).toggleClass('toggled');
    $('.navigation-wrapper').toggleClass('toggled');
});


// Input file name show

(function($, window, document, undefined)
{
  $('.button--file').each( function()
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

function changeUserImg(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.user-profile--profile-page').attr('style','background-image:url("'+ e.target.result + '")');
        }
        reader.readAsDataURL(input.files[0]);
        $('.user-profile--profile-page i').hide();
    }
}
$('.user-profile__action--change-picture').change(function(){
    changeUserImg(this);

    // Uncheck clear image if is checked.
    if ($('.user-profile__action--clear-picture').is(':checked')) {
      $('.user-profile__action--clear-picture').click();
    }
});

// Hide user image and change label when clear picture button is checked

$('.user-profile__action--clear-picture').change(function(){
  if ($(this).is(':checked')) {
    $(this).next('label').html('Cancelar remoção');
    $(this).next('label').removeClass('alert');
    $(this).next('label').addClass('warning');
    $('.user-profile--profile-page').addClass('no-bg');
    $('.user-profile--profile-page').html('<i class="icon icon-user" aria-hidden="true"></i>');
  } else {
    $(this).next('label').html('Remover');
    $('.user-profile--profile-page').html('');
    $(this).next('label').addClass('alert');
    $(this).next('label').removeClass('warning');
    $('.user-profile--profile-page').removeClass('no-bg');
  }
});
