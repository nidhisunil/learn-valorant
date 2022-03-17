function redirects(curr){
    window.location.href = "http://127.0.0.1:5000/agent/"+curr;
}

function myFunction() {
  confirm("Do you really want to discard changes? ");
}
function edit_entry(new_entry,curr_id){
  let iptAgent = new_entry["name"]
  let iptTut = new_entry["agent_tutorial"]
  let iptTrail = new_entry["agent_trailer"]
  let iptImg = new_entry["agent_image"]
  let iptDesc = new_entry["description"]
  let iptYr = new_entry["year_added"]
  let iptType = new_entry["agent_type"]
  let iptAb = new_entry["abilities"]
  let data_to_save = {"name": iptAgent, "agent_tutorial": iptTut, "agent_trailer": iptTrail, "agent_image": iptImg, "description": iptDesc, "abilities": iptAb, "year_added": iptYr, "agent_type": iptType, "id_rn":curr_id}
  console.log(data_to_save)
  $.ajax({
          type: "POST",
          url: "edit_entry",
          dataType : "json",
          contentType: "application/json; charset=utf-8",
          data : JSON.stringify(data_to_save),
          success: function(result){
              console.log("Success")
              let all_data = result["data"]
              data = all_data
              redirects(result["curr_id"])

          },
          error: function(request, status, error){
              console.log("Error");
              console.log(request)
              console.log(status)
              console.log(error)
          }
      });
}
$(document).ready(function(){


  $("#edit-submit").click(function(){
    let iptAgent = $("#input-agentt").val()
    let iptTut = $("#input-tutoriall").val()
    let iptTrail = $("#input-trailerr").val()
    let iptImg = $("#input-imagee").val()
    let iptDesc = $("#input-descriptionn").val()
    let iptYr = $("#input-yrr").val()
    let iptType = $("#input-agtypee").val()
    let iptAb = single_data["abilities"]
    let new_entry = {"name": iptAgent, "agent_tutorial": iptTut, "agent_trailer": iptTrail, "agent_image": iptImg, "description": iptDesc, "abilities": iptAb, "year_added": iptYr, "agent_type": iptType}

    edit_entry(new_entry,curr_id)

  })





})
