var currentRating = 0;

function showStars(starNumber) {

    //Save the current star selection
    currentRating = starNumber;

    //Load each star from the DOM
    var starArray = [$("#reviewStar0"), $("#reviewStar1"), $("#reviewStar2"), $("#reviewStar3"), $("#reviewStar4")];

    //If the star number is lower than the one that is being hovered over then set it to selected
    for (var i = 0; i <= starNumber; i++) {
        starArray[i].removeClass("glyphicon-star-empty");
        starArray[i].addClass("glyphicon-star");
    }

    //Otherwise set it to unselected
    for (var j = starNumber + 1; j <= 4; j++) {
        starArray[j].removeClass("glyphicon-star");
        starArray[j].addClass("glyphicon-star-empty");
    }

}

function saveReview(rated_username, rating_username) {

    var reviewComment = $("#reviewText").val();
    var reviewsTable = $("#reviewsTable");

    $.get('/submitreview/', {
        rating_user: rating_username,
        rated_user: rated_username,
        comment: reviewComment,
        rating: currentRating.toString()
    }, function (data) {

        if (data == "Rating confirmed") {

            var newHtml = reviewsTable.html();

            //Set URL - this URL will be changed to template version on next page refresh so this is temporary
            var newUrl = "/user/" + rating_username;
            newHtml += "<tr><td><h4><a href='" + newUrl + "'>" + rating_username + " </a>";

            for (var i = 0; i <= currentRating; i++)
                newHtml += "<span class='glyphicon glyphicon-star' aria-hidden='true'></span>";

            newHtml += "</h4><p>" + reviewComment + "</p></td></tr>";

            reviewsTable.html(newHtml);

            $("#reviewText").val("");

        }

    });

}
