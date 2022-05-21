$('.btn_nav').click(function() {
  // animate content
  $('.page__style').addClass('animate_content');
  $('.page__description').fadeOut(100).delay(2800).fadeIn();

  setTimeout(function() {
    $('.page__style').removeClass('animate_content');
  }, 3200);

  //remove fadeIn class after 1500ms
  setTimeout(function() {
    $('.page__style').removeClass('fadeIn');
  }, 1500);

});

// on click show page after 1500ms
$('.home_link').click(function() {
  setTimeout(function() {
    $('.home').addClass('fadeIn');
  }, 1500);
});

$('.projects_link').click(function() {
  setTimeout(function() {
    $('.projects').addClass('fadeIn');
  }, 1500);
});

$('.sala_link').click(function() {
  setTimeout(function() {
    $('.sala').addClass('fadeIn');
  }, 1500);
});

$('.sala-interna_link').click(function() {
  setTimeout(function() {
    $('.sala-interna').addClass('fadeIn');
  }, 1500);
});

$('.contact_link').click(function() {
  setTimeout(function() {
    $('.contact').addClass('fadeIn');
  }, 1500);
});

$('.quiz_link').click(function () {
  setTimeout(function () {
    $('.quiz').addClass('fadeIn');
  }, 1500);
});


var tamanhoPagina = 1;
var pagina = 0;

function paginar() {
  $('table > tbody > tr').remove();
  var tbody = $('table > tbody');
  for (var i = pagina * tamanhoPagina; i < dados.length && i < (pagina + 1) * tamanhoPagina; i++) {
    tbody.append(
      $('<tr>')
        .append(dados[i][0]).append(dados[i][1]).append(dados[i][2]).append(dados[i][3]).append(dados[i][4])
    )
  }
  $('#numeracao').text('Página ' + (pagina + 1) + ' de ' + Math.ceil(dados.length / tamanhoPagina));
}

function ajustarBotoes() {
  $('#proximo').prop('disabled', dados.length <= tamanhoPagina || pagina > dados.length / tamanhoPagina - 1);
  $('#anterior').prop('disabled', dados.length <= tamanhoPagina || pagina == 0);
}

$(function () {
  $('#proximo').click(function () {
    if (pagina < dados.length / tamanhoPagina - 1) {
      pagina++;
      paginar();
      ajustarBotoes();
    }
  });
  $('#anterior').click(function () {
    if (pagina > 0) {
      pagina--;
      paginar();
      ajustarBotoes();
    }
  });
  paginar();
  ajustarBotoes();
});