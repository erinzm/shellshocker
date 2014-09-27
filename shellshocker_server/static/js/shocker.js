$(document).ready(function() {
  alertTemplateText = $('#alertTemplateText').html();
  alertTemplate = Handlebars.compile(alertTemplateText);

  _.each(urlsToCheck, function (url) {
    _.each(headersToCheck, function (header) {
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
      }).fail(function () {
        console.log("Server request failed");
      });
    });
  });
  $('.testing-spinner').remove()
});
