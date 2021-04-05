/*
Defensive programming function that asks users to confirm in a modal
before deleting a question
*/

$(".delete-button").on("click", function(){
   let  questionId = $(this).data("question");
    $("#delete-confirm").attr("href", `/delete_question/${questionId}`);
});

/*
Function taken from https://getbootstrap.com/docs/4.0/components/forms/#tooltips to allow for form validation after form has been completed
*/
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();