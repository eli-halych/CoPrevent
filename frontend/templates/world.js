function clickToShowStep2() {
  var x = document.getElementById("step2WholeSurvey");
  // $("#reply").hide();
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  document.getElementById("anchorStep2").click();
}
