<script>
  $('.category-list__button')
    .click(function() {
      $(this).toggleClass('active');
      $.post('{% url "colab_edemocracia:update_prefered_theme" %}',
        {csrftoken: getCookie("csrftoken"),
         category_slug: $(this).attr('slug')}, null
      )

      var allCategoriesSelected = true
      $('.category-list__button').each(function() {
        if (!$(this).hasClass('active')) {
          allCategoriesSelected = false;
        }
      })

      if (allCategoriesSelected) {
        $('.button--select-all').addClass('deselect');
        $('.button--select-all').html('Deselecionar todos');
      } else {
        $('.button--select-all').removeClass('deselect');
        $('.button--select-all').html('Selecionar todos');
      }
  });

  $('.button--select-all')
    .click(function() {
      if ($('.button--select-all').hasClass('deselect')) {
        $('.category-list__button').removeClass('active');
        $('.button--select-all').removeClass('deselect');
        $('.button--select-all').html('Selecionar todos');
        $.post('{% url "colab_edemocracia:set_all_themes" %}',
          {csrftoken: getCookie("csrftoken"),
           action: 'deselect'}, null
        )
      } else {
        $('.category-list__button').addClass('active');
        $('.button--select-all').addClass('deselect');
        $('.button--select-all').html('Deselecionar todos');
        $.post('{% url "colab_edemocracia:set_all_themes" %}',
          {csrftoken: getCookie("csrftoken"),
           action: 'select'}, null
        )
      }
  });
</script>