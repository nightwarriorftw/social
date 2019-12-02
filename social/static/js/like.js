$(document).ready(function(event){
    $(document).on("click", "#like", function(event){
        event.preventDefault();
        var id = $(this).attr("value");
        console.log(id);
        $.ajax({
            type: "POST",
            url: "{% url 'feed:postDetails' %}",
            data: {
                "id": id,
                "csrfmiddlewaretoken": "{{csrf_token}}"
            },
            dataType: 'json',
            success: function(response){
                $("#like-section").html(response["form"]);
                console.log("Element changed");
            },
            error: function(rs, err){
                console.log(rs.responseText);
            }
        });
    })
})