$(document).ready(function() {
  _.each(urlsToCheck, function (url) {
    _.each(headersToCheck, function (header) {
      console.log('Checking URL ' + url + ' with header ' + header)
      $.post('/exploitable', {
        websiteUrl: url,
        header: header
      }).done(function (response) {
        exploitable = response['exploitable'];
        console.log("This URL is exploitable? " + exploitable);
      }).fail(function () {
        console.log("Server request failed");
      });
    });
  });
  $('.testing-spinner').remove()
});
