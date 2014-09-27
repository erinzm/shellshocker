// When the document is ready
$(document).ready(function() {
  // Grab the Handlebars template from a <script> tag
  alertTemplateText = $('#alertTemplateText').html();
  // Compile the Handlebars template
  alertTemplate = Handlebars.compile(alertTemplateText);

  // For every index of urlsToCheck
  for (var i = 0; i < urlsToCheck.length; i++){
    // Get the element with that index
    url = urlsToCheck[i]
    // For every index of headersToCheck
    for (var j = 0; j < headersToCheck.length; j++) {
      // Get the element with that index
      header = headersToCheck[j]
      // Define an empty response
      var response = "";
      //console.log('Checking URL ' + url + ' with header ' + header);
      $.ajax({
        type: 'POST',
        async: false,
        url: exploitableCheckURL,
        data: {
          websiteUrl: url,
          header: header
        },
        success: function(result) {
          // Is it exploitable?
          exploitable = result['exploitable'];
          //console.log("This URL is exploitable? " + exploitable);
          // Generate the HTML of the template
          template_html = alertTemplate({exploitable: exploitable, url: url, header: header});
          // Append it to the results well
          $('.results-well').append(template_html).fadeIn();
          //console.log(template_html);
        }
      });
    }
  }

  // It's all done, hide the spinner ;)
  $('.testing-spinner').hide();
});
