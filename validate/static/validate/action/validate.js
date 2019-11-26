$(".hidden").hide();

$("#entrance_id").val("");

$("input[type='submit']").click(function(event) {
    event.preventDefault();

    var require = $("#require");
    var fail = $("#fail");
    var success = $("#success");

    require.hide();
    fail.hide();
    success.hide();

    var regex = "^[0-9]{2}/[0-9]{5}$";

    var entrance_id = $("input[name='entrance_id']").val();

    if (entrance_id == "") {
        require.html("<strong>Entrance ID</strong> is required!");
        require.fadeIn();
    } else if (!entrance_id.match(regex)) {
        require.html("<strong>Invalid Entrance ID</strong> format!");
        require.fadeIn();
    } else {
        $.ajax({
            url: "/ajax/checkValidate/",
            type: 'GET',
            data: entrance_id,
            mimeType: 'application/json',
            contentType: 'application/json',
            dataType: 'json',
            success: function(status) {
                if (status == null) {
                    fail.html("<strong>Failed!</strong> Something went wrong. Please try again.");
                    fail.fadeIn();
                } else {

                    if (status.validated) {
                        fail.html("The Entrance ID <strong>" + entrance_id + "</strong> is already <strong>Validated!</strong>");
                        fail.fadeIn();
                    } else {
                        $("#eid").html(entrance_id);
                        success.fadeIn();
                        $("#entrance_id").val("");
                    }
                }

            },
            error: function(data, status, xhr) {
                fail.html("<strong>Failed!</strong> Something went wrong. Please try again.");
                fail.fadeIn();
            }
        });

    }

});