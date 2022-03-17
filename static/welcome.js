function displayNames(popular){
    //empty old data
    $("#popular-container").empty()

    //insert all new data
    $.each(popular, function(i, datum){
        let new_name = $("<div class='small-popular-container col-md-4'>")
        let temp_id=datum["id"]
        let list_item = $("<a href='/agent/" +temp_id+ "' class='pop-links'>")
        list_item.html("Learn "+datum["name"])
        let list_image_source = datum["agent_image"]
        let list_desc = $("<p class='entice-me'>")
        list_desc.html(datum["description"])
        let list_image = $("<img src='"+list_image_source+"' alt='character-image' class='popular-img' href='/agent/" +temp_id+ "'>")

        new_name.append(list_image)
        new_name.append(list_desc)
        new_name.append(list_item)
        $("#popular-container").append(new_name)
    })
}



$(document).ready(function(){
    //when the page loads, display all the names
    displayNames(popular)



})
