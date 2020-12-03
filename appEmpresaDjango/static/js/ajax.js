$(document).ready(function() {

  $('section.post > header.post-header > h2.post-title > a').each(function () {
    var href = $(this).attr("href");
    href = href.replace("post", "postAjax");
    $(this).qtip({
       content: {
          url: href,
          method: 'get'
       }
    });
  });

});