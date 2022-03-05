$(document).ready(function () {
          // отслеживаем событие отправки формы
          // $('#contactForm').submit(function () { // по кнопке submit click keyup
          $('#target').click(function () {
              // создаем AJAX-вызов
              $.ajax({
                  data: $(this).serialize(), // получаем данные формы
                  type: $(this).attr('method'), // GET или POST
                  // url: "{% url 'contact_form.html' %}",
                  // если успешно, то
                  success: function (response) {
                  },
                  // если ошибка, то
                  error: function (response) {
                      // предупредим об ошибке
                      alert(response.responseJSON.errors);
                      console.log(response.responseJSON.errors)
                  }
              });
              return false;
          });
      })