function post(url, data) {
  // Return a new promise.
  return new Promise(function(resolve, reject) {
    // Do the XHR HTTP stuff
    request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    request.onload = function() {
      if (request.status >= 200 && request.status < 400){
        // Success!
        resolve({response: JSON.parse(request.response), dat: data});
      } else {
        // We reached our target server, but it returned an error
        reject(Error(request.statusText));
      }
    };

    request.onerror = function() {
      // There was a connection error of some sort
      reject(Error("Network Error"));
    };

    request.send($.param(data));
  });
}
