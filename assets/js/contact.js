window.onload = function(){
  document.getElementById("error_message").style.visibility = 'hidden';
  document.getElementById("sent-message").style.visibility = 'hidden';
};


$("#contactBtn").on('click', function(){

    var name = $("#name").val();
    var email = $("#email").val();
    var subject = $("#subject").val();
    var message = $("#message").val();
    var csrf = $('#csrf_form').find('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: "home/create-contact/",
        dataType: "json",
        type:"POST",
        data:{'name':name, 'email':email, 'subject':subject, 'message': message, 'csrfmiddlewaretoken': csrf},
        async:false,
        success: function(result){
              var resp_obj = JSON.stringify(result);
              if (result.success){
                document.getElementById("sent-message").style.visibility = 'visible';
                  $("#sent-message").empty();
                  $("#error_message").empty();
                  $('#sent-message').append(JSON.stringify(result['success']))
		        }
		      else {
                     document.getElementById("error_message").style.visibility = 'visible';
                     $("#error_message").empty();
                     $("#sent-message").empty();
                     $('#error_message').append("Errors:" + JSON.stringify(result['errors']).replace('{','').replace('}','').replace('[','').replace(']',''))
		           }

        },
        error: function(xhr,status,errorThrown){
                    alert("Something Went Wrong!");
						 }
    });


  });