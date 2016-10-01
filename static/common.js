function toggleShowAddFriend(){
    if($("#addfrienddiv").is(":visible")) {
        $("#addfrienddiv").hide(); 
    } else {
        $("#addfrienddiv").show();
    }
}

function toggleShowDeleteFriend(){
    if($("#deletefrienddiv").is(":visible")) {
        $("#deletefrienddiv").hide(); 
    } else {
        $("#deletefrienddiv").show();
    }
}

function toggleShowUpdateFriend(){
    if($("#updatefrienddiv").is(":visible")) {
        $("#updatefrienddiv").hide(); 
    } else {
        $("#updatefrienddiv").show();
    }
}

function putFriend() {
    name= $("#updatefriends").val(),
    add = $("#updateadd").val(),
    phoneno= $("#updatephoneno").val(), 
    email= $("#updateemail").val(), 
    birthday =  $("#updatebirthday").val()

    newURL = window.location.href + "?name=" + name + "&add=" + add + "&phoneno=" + phoneno + "&email=" + email + "&birthday=" + birthday;
    window.location.replace(newURL);

    // $.ajax({
    //     url: window.location.href + "?name=" + name + "&add=" + add + "&phoneno=" + phoneno + "&email=" + email + "&birthday=" + birthday,
    //     type: "PUT",
    //     success: function() {
    //         alert("PUT COMPLETED");
    // }
    // });

}