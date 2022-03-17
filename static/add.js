function add_alert_div(alert_id){
  $("#alert-row").empty()
  var alertsbox = $("<div class='alert alert-success' role=alert'>")
  alertsbox.html("Success! View your added element <a href='/agent/"+alert_id+"' >here</a>")
  $("#alert-row").append(alertsbox)



  $("#input-agent").val("")
  $("#input-tutorial").val("")
  $("#input-trailer").val("")
  $("#input-image").val("")
  $("#input-description").val("")
  $("#input-ab1").val("")
  $("#input-ab2").val("")
  $("#input-ab3").val("")
  $("#input-ab4").val("")
  $("#input-yr").val("")
  $("#input-agtype").val("")
  $("#input-agent").focus()
}

function save_entry(new_entry){
  let iptAgent = new_entry["name"]
  let iptTut = new_entry["agent_tutorial"]
  let iptTrail = new_entry["agent_trailer"]
  let iptImg = new_entry["agent_image"]
  let iptDesc = new_entry["description"]
  let iptYr = new_entry["year_added"]
  let iptType = new_entry["agent_type"]
  let iptAb = new_entry["abilities"]

  if (iptAgent == ""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#name-label").append(tempWarn)
    $("#input-agent").focus()
  }
  else if(iptTut==""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#tutorial-label").append(tempWarn)
    $("#input-tutorial").focus()
  }
  else if(iptTrail==""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#trailer-label").append(tempWarn)
    $("#input-trailer").focus()
  }
  else if(iptImg ==""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#image-label").append(tempWarn)
    $("#input-image").focus()
  }
  else if(iptDesc ==""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#desc-label").append(tempWarn)
    $("#input-description").focus()
  }
  else if(iptYr==""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#year-label").append(tempWarn)
    $("#input-yr").focus()
  }
  else if(iptType =""){
    $(".warning-text").remove()
    var tempWarn = $("<span class='warning-text'>")
    tempWarn.html("Can't be empty")
    $("#type-label").append(tempWarn)
    $("#input-agtype").focus()
  }

  else{
    $(".warning-text").remove()
    let data_to_save = {"name": iptAgent, "agent_tutorial": iptTut, "agent_trailer": iptTrail, "agent_image": iptImg, "description": iptDesc, "abilities": iptAb, "year_added": iptYr, "agent_type": iptType}
    $.ajax({
            type: "POST",
            url: "save_entry",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                console.log("Success")
                let all_data = result["data"]
                data = all_data
                add_alert_div(result["alert_id"])
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
  }


}


$(document).ready(function(){
  $("#post-button").click(function(){
    let iptAgent = $("#input-agent").val()
    let iptTut = $("#input-tutorial").val()
    let iptTrail = $("#input-trailer").val()
    let iptImg = $("#input-image").val()
    let iptDesc = $("#input-description").val()
    let ab1 = $("#input-ab1").val()
    let ab2 = $("#input-ab2").val()
    let ab3 = $("#input-ab3").val()
    let ab4 = $("#input-ab4").val()
    let iptYr = $("#input-yr").val()
    let iptType = $("#input-agtype").val()
    let iptAb = [ab1,ab2,ab3,ab4]
    let new_entry = {"name": iptAgent, "agent_tutorial": iptTut, "agent_trailer": iptTrail, "agent_image": iptImg, "description": iptDesc, "abilities": iptAb, "year_added": iptYr, "agent_type": iptType}
    save_entry(new_entry)

  })



})
