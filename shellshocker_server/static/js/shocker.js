$(document).ready(function() {
  alertTemplateText = $('#alertTemplateText').html();
  alertTemplate = Handlebars.compile(alertTemplateText);

  for (var i = 0; i < urlsToCheck.length; i++){
    url = urlsToCheck[i]
    for (var j = 0; j < headersToCheck.length; j++) {
      header = headersToCheck[j]
      console.log('Checking URL ' + url + ' with header ' + header)
      $.post(exploitableCheckURL, {
        websiteUrl: url,
        header: header
      }).done(function (response) {
        exploitable = response['exploitable'];
        console.log("This URL is exploitable? " + exploitable);
        template_html = alertTemplate({exploitable: exploitable, url: url, header: header});
        $('.results-well').append(template_html).fadeIn();
        console.log(template_html);
        $('.testing-spinner').remove()
      }).fail(function () {
        console.log("Server request failed");
      });
    }
  }
});
