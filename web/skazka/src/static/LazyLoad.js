document.addEventListener("DOMContentLoaded", function () {
  let lazyImage = document.getElementById("objectImage");
  if (lazyImage.dataset.src) {
    lazyImage.src = lazyImage.dataset.src;
  }
});
