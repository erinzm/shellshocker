// When the document is ready
$(document).ready(function() {
  // Grab the Handlebars template from a <script> tag
  alertTemplateText = $('#alertTemplateText').html();
  // Compile the Handlebars template
  alertTemplate = Handlebars.compile(alertTemplateText);

  exploits = _.flatten(
    _.map(urlsToCheck, function (url) {
      return _.map(headersToCheck, function (header) {
        return {url: url, header: header};
      });
    }),
    true);

  console.log(exploits);

  exploits.reduce(function (sequence, exploit) {
    return sequence.then(function () {
      console.log(exploit);
      return post(exploitableCheckURL, {websiteUrl: exploit.url, header: exploit.header});
    }).then(function(result) {
      console.log(result);
      // Generate the HTML of the template
      template_html = alertTemplate({exploitable: result.response.exploitable, url: result.dat.websiteUrl, header: result.dat.header});
      // Append it to the results well
      $('.results-well').append(template_html).fadeIn();
      //console.log(template_html);
    }).then(function () {
      // It's all done, hide the spinner ;)
      //$('.testing-spinner').hide();
    });
  }, Promise.resolve());
});
