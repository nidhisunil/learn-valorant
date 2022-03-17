$(document).ready(function(){
  $( "#search-pressed" ).click(function( ) {
      let text = $("#search-text").val()
      if (text == " "){
        $$("#search-text").val('')
      }else{
      window.location.href = "http://127.0.0.1:5000/search/"+text;}
});
$(document).on('keypress','#search-text',function(e) {
        if(e.which == 13) {
          let text = $("#search-text").val()
          if (text == " "){
            $$("#search-text").val('')
          }else{
          window.location.href = "http://127.0.0.1:5000/search/"+text;}
        }
    })


})
