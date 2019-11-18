$(document).ready( function(event){
    $(document).on('click', '#like', function(event){
        event.preventDefault();
        var pk = $(this).attr('value');
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        console.log(csrftoken);
        console.log(pk);
        $.ajax({
            type: 'POST',
            url : "like/",
            data: {
                "id": pk,
                'csrfmiddlewaretoken': csrftoken
            },
            dataType: 'json',
            success: function(response){
                $("#like-section").html(response["total_likes"])
                console.log(
                    $("#like-section").html(response["total_likes"])
                )
            },
            error: function(rs, e){
                console.log(rs.responseText);
            },
        });      
    });
});