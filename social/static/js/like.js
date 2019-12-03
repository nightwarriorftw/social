$(document).ready(function(event){
    $(document).on("click", "#like", function(event){
        event.preventDefault();
        var id = $(this).attr("value");
        console.log(id)
        const token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        $.ajax({
            type: "POST",
            url: "/feed/like/",
            data: {
                "id": id,
                "csrfmiddlewaretoken": token
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