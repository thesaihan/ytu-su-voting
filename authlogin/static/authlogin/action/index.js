$(".hidden").hide();

$("input[type='submit']").click(function(event) {
    event.preventDefault();

    var require = $("#require");
    var fail = $("#fail");

    require.hide();
    fail.hide();

    var username = $("input[name='username']").val();
    var password = $("input[name='password']").val();

    if (username == "" && password == "") {
        require.html("<strong>Username &amp; Password</strong> are required!");
        require.fadeIn();
    } else if (username == "") {
        require.html("<strong>Username</strong> is required!");
        require.fadeIn();
    } else if (password == "") {
        require.html("<strong>Password</strong> is required!");
        require.fadeIn();
    } else {
        $.ajax({
            url: "/ajax/checkAdmin/",
            type: 'GET',
            data: username + "|" + password,
            mimeType: 'application/json',
            contentType: 'application/json',
            dataType: 'json',
            success: function(admin) {
                if (admin == "" || admin == null)
                    fail.fadeIn();
                else
                    $("form").submit();

            },
            error: function(data, status, xhr) {
                fail.fadeIn();
            }
        });

    }

});