function displayLinks(lists){
  $("#search-results-container").empty()
  if (lists.length==0){
    var outer = $("<h2 class='empty-results-container'>")
    outer.html("No matches found")
    $("#search-results-container").append(outer)
  }
  else{
    $.each(lists, function(i, datum){
      var outer = $("<div class='small-links-container col-md-4'>")
      var temp1 = datum['id']
      var temp2 = datum['name']
      var temp3 = datum['year_added']
      var temp4 = datum['agent_image']
      var temp5 = datum['agent_type']
      var second_inner = $("<img src='"+temp4+"' alt='img-of-character' class='popular-img'>")
      var first_inner = $("<div class='year-text'>")
      var third_inner = $("<div class='type-text'>")
      first_inner.html("Year Added: <span class='green-text'>"+temp3+"</span>")
      third_inner.html("Agent Type: <span class='green-text'>"+temp5+"</span>")
      var inner = $("<a href='/agent/"+temp1+"' class='green-text underlines'>")
      inner.html(temp2)

      outer.append(inner)
      outer.append(first_inner)
      outer.append(third_inner)
      outer.append(second_inner)
      $("#search-results-container").append(outer)
    })
  }
}


$(document).ready(function(){
    //when the page loads, display all the names
    displayLinks(lists)
})
