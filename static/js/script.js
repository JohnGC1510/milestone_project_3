
$(".delete-button").on("click", function(){
   let  questionId = $(this).data("question");
    $("#delete-confirm").attr("href", `/delete_question/${questionId}`);
});

