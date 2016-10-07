    function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
              for (var i = 0; i < cookies.length; i++) {
                  var cookie = jQuery.trim(cookies[i]);
                  // Does this cookie string begin with the name we want?
                  if (cookie.substring(0, name.length + 1) == (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
      }
      function isvalid(pass){
      	 var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
		return re.test(pass);

      }
     // function redirection(){
      //	window.location.replace("http://127.0.0.1:8000/myaccount/login/");
      //}


    function updateinformation(){
      fname = document.getElementById('fname').value;
      lname = document.getElementById('lname').value;
      newpassword = document.getElementById('npassword').value;


          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
                  //document.getElementById("demo").innerHTML = this.responseText;
                  //document.getElementById("request_panel").innerHTML = this.responseText + document.getElementById("request_panel").innerHTML;
              }
          };
          xhttp.open("POST", "updatepersonalinfo/", true);
          var csrftoken = getCookie('csrftoken');

          xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
          xhttp.setRequestHeader("X-CSRFToken", csrftoken);
          query = "fname="+fname;
          query +="&lname="+lname;
          query +="&npassword="+newpassword;
          if(isvalid(newpassword)){
          		xhttp.send(query);
          		console.log('okayyy');
          		document.getElementById('error').innerHTML="Success";
        //  		redirection(); 
          			
          }
          else{
                document.getElementById('error').innerHTML="Error";
          }
          
    }
