// fetch('/read')
// .then(function(response) {
//   return response.text();
// })
// .then(function(response) {
//   document.querySelector(".messageboard").innerText= response
// })
//
// confirm("It is worth a try")

document.addEventListener("DOMContentLoaded", function() {



  var b = document.querySelector(".Colour")
  console.log(b.value)

  fetch('/read')
    .then(function responseFunction(response) {
      return response.text();
    })
    .then(function(response) {
      document.querySelector(".messageboard").innerText = response
    })
});
