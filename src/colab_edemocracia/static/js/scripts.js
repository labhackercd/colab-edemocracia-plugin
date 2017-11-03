$(document).click(function(e) {
    var target = e.target
    if (!$(target).closest('.toggled').length) {

      $('.toggled')
        .removeClass('toggled');
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
