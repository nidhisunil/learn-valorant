function displayAgents(single_data){
    //empty old data
    $("#agent-cont").empty()

    //insert all new data
    $.each(single_data["abilities"], function(i, datum){
        let item = $("<li class='list-ab'>")
        item.html(datum)
        $("#agent-cont").append(item)

    })
}



$(document).ready(function(){
    //when the page loads, display all the names
    displayAgents(single_data)



})
