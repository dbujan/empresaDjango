$(document).ready(function() {

  $("div.posts > h1.content-subhead").click(function () {
    $("div.post-description").slideUp();
  });

  $("div.posts > h1.content-subhead").dblclick(function () {
    $("div.post-description").slideDown();
  });
  
 });