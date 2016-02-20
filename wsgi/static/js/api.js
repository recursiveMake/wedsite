/**
 * Created by adonis on 2/20/2016.
 */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            var csrftoken = $.cookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function submit_rsvp(event, api_url) {
    console.warn('Submitting...');
    event.stopPropagation();
    var form_data = $('#rsvp-form').serialize();
    $.ajax({
        method: "POST",
        url: api_url,
        data: form_data,
        success: function(returned_data, status_text, jqXHR_object) {
            console.warn('AJAX request successful');
            var response = returned_data;
            if ( response.success ) {
                console.warn('Response success');
                $( '#rsvp-div' ).html( response.data );
                $( '#rsvp-modal' ).modal('hide');
            }
            else {
                console.warn('Response failed');
                $( '#rsvp-form').html( returned_data.data );
            }
        },
        error: function(jqXHR_object, status_text, error_thrown) {
            console.warn('AJAX request failed');
            $( '#rsvp-form-invitation' ).html("<p id='rsvp-form-invitation'>An unknown error occurred. Please try again.</p>");
        },
        timeout: 5000
    });
}

function display_rsvp_modal() {
    $('#rsvp-modal' ).modal();
}
