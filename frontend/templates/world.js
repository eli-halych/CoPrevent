function clickToShowStep2() {
  var x = document.getElementById("step2WholeSurvey");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  //calling step2 anchor
  document.getElementById("anchorStep2").click();
}
function checkRegionCode(regionCode) {
  if (regionCode.localeCompare("US") == 0) {
    console.log("hello,it works");
  } else if (regionCode.localeCompare("CN") == 0) {
    console.log("hello,it works too");
  }
}
