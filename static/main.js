function startLoading() {
    
    var btn = document.getElementById("loading-btn");
    var barContainer = document.getElementById("loading-bar-container");
    var bar = document.getElementById("loading-bar");
    btn.disabled = true;
    btn.style.opacity = 0.5;
    barContainer.style.display = "block";
    
    // Simulate a long-running task
    var startTime = new Date().getTime();
    var interval = setInterval(function() {
      var currentTime = new Date().getTime();
      var elapsed = currentTime - startTime;
      if (elapsed >= 15000) {
        clearInterval(interval);
        btn.disabled = false;
        btn.style.opacity = 1;
        barContainer.style.display = "none";
        bar.style.width = "100%";
      } else {
        var progress = elapsed / 15000;
        bar.style.width = (progress * 100) + "%";
      }
    }, 100);
    
  }