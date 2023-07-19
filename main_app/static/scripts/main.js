console.log("hello world")
$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  
  $('.panel-tabs a').on('click', function(e) {
    e.preventDefault();

    // Remove 'is-active' class from all tabs and add it to the current tab
    $('.panel-tabs a').removeClass('is-active');
    $(this).addClass('is-active');

    // Hide all gear items first
    $('.gear-item').hide();

    // Get tab name
    let tabName = $(this).text().trim().toLowerCase();

    // Replace spaces with underscores
    tabName = tabName.replace(/\s+/g, '_');

    // If 'All' tab is clicked, show all items, else show only the related gear items
    if(tabName === 'all') {
      $('.gear-item').show();
    } else {
      $('.' + tabName).show();
    }
  });

  // Reset button logic
  $('.button.is-link.is-outlined.is-fullwidth').on('click', function(e) {
    e.preventDefault();

    // Hide all gear items
    $('.gear-item').hide();

    // Uncheck the checkbox
    $('.panel-block input[type="checkbox"]').prop('checked', false);

    // Remove active class from all tabs and add it back to 'All' tab
    $('.panel-tabs a').removeClass('is-active');
    $('.panel-tabs a').first().addClass('is-active');

    // Show all gear items
    $('.gear-item').show();
  });

$(".dropdown").click(function (event) {
    $(this).toggleClass("is-active");
  });