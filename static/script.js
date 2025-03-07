document.addEventListener("DOMContentLoaded", function () {
  // Initialize CodeMirror (or another editor)
  var editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
    mode: "python",
    lineNumbers: true,
    autoCloseBrackets: true,
    theme: "default",
    autoRefresh: true
  });

});


/*
setTimeout(function() {
    document.getElementById("loading-screen").style.display = "none";
    document.getElementById("main").style.display = "block";
    
    },2700);
    */

var typed = new Typed("#text_mok", {
    strings: ["Join us to<br>learn program like <span style='color: rgb(255, 255, 255);'>spider web.</span>"],
    typeSpeed: 50,
    showCursor: false
  });
  
  var typed2 = new Typed("#text_mok2", {
    strings: ["<b><span style='color: #0116FF;'>#include</span>&lt;<span style='color: #F31BAB;'>iostream</span>&gt;<br> \
               using namespace <span style='color: #0116FF;'>std;</span><br> \
               <span style='color: #0116FF;'>int</span> main() {<br> \
               // <span style='color: #00FFE1;'>Welcome message for<br>Spider Coding visitors</span><br> \
               cout << <span style='color: #EEFF00;'>\"Hi! Welcome to Spider Coding!<br>you can learn with us how to become<br>programmer\"</span> << endl;<br> \
               <span style='color: #0116FF;'>return</span> 0; }</b>"],
    typeSpeed: 25
  });

  function show_all_py(){
    document.getElementById("main_courses").style.display = "none";
    document.getElementById("main_courses_py").style.display = "block";
  }
  function show_quizzes(){
    document.getElementById("random").style.display = "none";
    document.getElementById("quizzes").style.display = "flex";

  }
  function show_random(){
    document.getElementById("quizzes").style.display = "none";
    document.getElementById("random").style.display = "flex";
  }
  function more_details_py(){
    document.getElementById("main_courses_py").style.display = "none";
    document.getElementById("python_cour_beg").style.display = "flex";
  }
  function show_problem(){
    document.getElementById("type_of_courses").style.display = "none";
    document.getElementById("levels_of_problems").style.display = "block";
  }

  window.onload = function() {
    document.getElementById('CERETERS_btn').click();}

  let hassan_div = document.getElementById('hassan_div')
  let abdullah_div = document.getElementById('abdullah_div')



  function writeToCERETERS(){
    hassan_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>hassan abdulhadi</b></h1>
                    <p style="font-size: 1vw; margin-top: 1vw;">Hello my name is hassan<br> and i full<br> stack developer </p>`
    abdullah_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>abdullah jalal</b></h1>
                    <p style="font-size: 1vw; margin-top: 1vw;">Hello my name is abdullah<br> and i full<br>
                      stack developer </p>`

  }

  function writeToSocial(){
    hassan_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>hassan abdulhadi</b></h1>
    <p style="font-size: 1vw; margin-top: 1vw;">
      <a href="">

                        <i class="icon_socal bi bi-linkedin text-2xl mr-2"></i>
                    </a>
      <a href="">

                        <i class="icon_socal bi bi-facebook text-2xl mr-2"></i>
                    </a>
      <a href="">

                        <i class="icon_socal bi bi-instagram text-2xl mr-2"></i>
                    </a>
    
    
    </p>`
    abdullah_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>abdullah jalal</b></h1>
    <p style="font-size: 1vw; margin-top: 1vw;">
    <a href="">

                        <i class="icon_socal bi bi-linkedin text-2xl mr-2"></i>
                    </a>
                    <a href="">

                        <i class="icon_socal bi bi-facebook text-2xl mr-2"></i>
                    </a>
                          <a href="">

                        <i class="icon_socal bi bi-instagram text-2xl mr-2"></i>
                    </a>
    
    
    </p>`

  }





  function writeToGithub(){
    hassan_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>hassan abdulhadi</b></h1>
    <p style="font-size: 1vw; margin-top: 1vw;">
     username:hassanmok
    URL:<a style="color:blue;onclick:pink;" href="https://github.com/hassanmok">https://github.com/hassanmok</a>

    
    
    </p>`
    abdullah_div.innerHTML=`<h1 style="font-size: 1.5vw;"><b>abdullah jalal</b></h1>
    <p style="font-size: 1vw; margin-top: 1vw;">
      username:AbdullahG5
     URL:<a style="color:blue;" href="https://github.com/AbdullahG5">https://github.com/AbdullahG5</a>
    
    </p>`

  }





  document.getElementById("update-btn").addEventListener("click", function() {
    let countElement = document.getElementById("current-count");
    let progressBar = document.getElementById("progress-bar");

    if (!countElement || !progressBar) {
        console.error("❌ ERROR: Elements not found!");
        return;
    }

    let countValue = parseInt(countElement.textContent.trim(), 10);
    if (isNaN(countValue)) {
        console.error("❌ ERROR: Invalid count value:", countElement.textContent);
        countValue = 0; // Default to 0 if invalid
    }

    let maxValue = 10;  // Adjust this as needed
    let progressPercentage = (countValue / maxValue) * 100;

    console.log(`✅ Updating progress to: ${progressPercentage}%`);

    // ✅ Apply the width change CORRECTLY
    progressBar.style.width = progressPercentage + "%";
    progressBar.setAttribute("aria-valuenow", progressPercentage);
});


