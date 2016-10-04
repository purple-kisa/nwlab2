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
    data = {
        name : $("#updatefriends").val(),
        add : $("#updateadd").val(),
        phoneno : $("#updatephoneno").val(), 
        email : $("#updateemail").val(), 
        birthday :  $("#updatebirthday").val()

    }

    // newURL = window.location.href + "?name=" + name + "&add=" + add + "&phoneno=" + phoneno + "&email=" + email + "&birthday=" + birthday;
    // window.location.replace(newURL);

    $.ajax({
        url: window.location.href,
        type: "PUT",
        contentType: "application/json", 
        data: JSON.stringify(data),
        success: function() {
            window.location.reload();
        }
    });

}

function postAddWithJson() {
    data = {
        name : $("#addname").val(),
        add : $("#addaddress").val(),
        phoneno : $("#addphoneno").val(), 
        email : $("#addemail").val(), 
        birthday :  $("#addbirthday").val()

    }

    console.log(JSON.stringify(data))

    $.ajax({
        url: window.location.href, 
        type: "POST", 
        contentType: "application/json",
        data: JSON.stringify(data), 
        success: function() {
            window.location.reload();
        }
    })

}

function deleteWithJson() {
    data = {
        name : $("#deletefriends").val()

    }
    console.log(data)

    $.ajax({
        url: window.location.href, 
        type: "DELETE", 
        contentType: "application/json",
        data: JSON.stringify(data), 
        success: function() {
            window.location.reload();
        }
    })

}