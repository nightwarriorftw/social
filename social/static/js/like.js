$(document).ready( function(event){
    $(document).on('click', '#like', function(event){
        event.preventDefault();
        var pk = $(this).attr('value');
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        console.log(csrftoken);
        console.log(pk);
        $.ajax({
            type: 'POST',
            url : '{% url "feed:like_post" %}/',
            data: {
                "id": pk,
                'csrfmiddlewaretoken': csrftoken
            },
            dataType: 'json',
            success: function(response){
                $("#like-section").html(response['form']);
                console.log("Like/Dislike section done")
            },
            error: function(rs, e){
                console.log(rs.responseText);
            },
        });      
    });
});