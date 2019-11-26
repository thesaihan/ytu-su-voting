var selectedChairman = 0;
var selectedSecretary = 0;
var selectedArt = 0;
//var selectedLiterature=0;

/*
$(".container").css("paddingLeft","0px");
$(".container").css("paddingRight","0px");
*/
/*
var w=$(window).width();
$("#chairmanGroup").css("width",w+"px");
$("#chairmanGroup").css("marginLeft","0px");

$(window).resize(function(){
	var w=$(window).width();
	$("#chairmanGroup").css("width",w+"px");
	$("#chairmanGroup").css("marginLeft","0px");
});
*/
$(".card").addClass("shadow");
$("#entrance_id").val("");

$("input[type='submit']").click(function(event) {
    event.preventDefault();
    /*
    alert("Selected Chairman : "+selectedChairman
    		+"\nSelected Secretary : "+selectedSecretary
    );
    */

    var voteForm = $("#voteForm");

    var entrance_id = $("#entrance_id").val();

    var errors = "";

    if (selectedChairman == 0)
        errors += "Please select your vote for <span style='color:brown'><strong>Chairman</strong></span>.<br>";
    else
        voteForm.append($("<input type='hidden' name='selectedChairman' value='" + selectedChairman + "'/>"));

    if (selectedSecretary == 0)
        errors += "Please select your vote for <span style='color:brown'><strong>Secretary</strong></span>.<br>";
    else
        voteForm.append($("<input type='hidden' name='selectedSecretary' value='" + selectedSecretary + "'/>"));

    if (selectedArt == 0)
        errors += "Please select your vote for <span style='color:brown'><strong>Art Officer</strong></span>.<br>";
    else
        voteForm.append($("<input type='hidden' name='selectedArt' value='" + selectedArt + "'/>"));

    //if(selectedLiterature==0)
    //	errors+="Please select your vote for <span style='color:brown'><strong>Literature Officer</strong></span>.<br>";
    //else
    //	voteForm.append($("<input type='hidden' name='selectedLiterature' value='"+selectedLiterature+"'/>"));

    var regex = "^[0-9]{2}/[0-9]{5}$";
    if (entrance_id == "")
        errors += "Enter your <span style='color:brown'><strong>Entrance ID</strong></span>!";
    else if (!entrance_id.match(regex))
        errors += "Invalid <span style='color:brown'><strong>Entrance ID</strong></span> format!";
    else
        voteForm.append($("<input type='hidden' name='entrance_id' value='" + entrance_id + "'/>"));

    if (errors != "") {
        $(".lead").html("");
        $(".lead").append(errors);
        $("#afterVoteModal").modal('show');
    } else {
        $.ajax({
            url: "/ajax/checkVote/",
            type: 'GET',
            data: entrance_id,
            mimeType: 'application/json',
            contentType: 'application/json',
            dataType: 'json',
            success: function(vote) {

                //console.log(typeof vote.isVoted);
                //console.log("isVoted : " + vote.isVoted);
                //console.log("isValidated : " + vote.isValidated);

                if (vote.isValidated == false)
                    errors += "Your ID hasn't been validated yet!<br>" +
                    "Please proceed to the Voting Registration Counter first.";

                else if (vote.isVoted == true)
                    errors += "You have voted!<br>" +
                    "If you haven't actually voted, please report the problem to the voting committee.";

                if (errors != "") {
                    $(".lead").html("");
                    $(".lead").append(errors);
                    $("#afterVoteModal").modal('show');
                } else
                    voteForm.submit();

            },
            error: function(data, status, xhr) {
                alert("Oops! Something went wrong!");
            }
        });

    }

});

$(".card").click(function() {

    let id = $(this).attr("id");
    let idType = id.slice(0, 1);
    let idNum = id.slice(-1, id.length);
    let idSpan = idType + idNum;

    let span = $("<span/>");
    span.addClass("badge");
    span.addClass("badge-pill");
    span.addClass("badge-dark");
    span.html("selected");

    $("h5[id^='" + idType + "']").each(function() {
        if ($(this).attr("id") == idSpan) {
            $(this).html("");
            $(this).append(span);
            //$("div[id='"+id+"']").css({border:"3px solid gray"});
            //card.addClass("shadow");
        } else {
            $(this).html("<br>");
            //$("div[id='"+id+"']").css({border:"1px solid lightgray"});
            //card.removeClass("shadow");
        }

    });

    if (idType == "c")
        selectedChairman = idNum;
    if (idType == "s")
        selectedSecretary = idNum;
    if (idType == "a")
        selectedArt = idNum;

    //if(idType=="l")
    //	selectedLiterature = idNum;

});