const displayTime = document.querySelector(".display-time");
// Time
function showTime() {
    let time = new Date();
    displayTime.innerText = time.toLocaleTimeString("en-US", { hour12: false });
    setTimeout(showTime, 1000);
}

showTime();

// Date
function updateDate() {
    let today = new Date();

    // return number
    let dayName = today.getDay(),
        dayNum = today.getDate(),
        month = today.getMonth(),
        year = today.getFullYear();

    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    const dayWeek = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    // value -> ID of the html element
    const IDCollection = ["day", "daynum", "month", "year"];
    // return value array with number as a index
    const val = [dayWeek[dayName], dayNum, months[month], year];
    for (let i = 0; i < IDCollection.length; i++) {
        document.getElementById(IDCollection[i]).firstChild.nodeValue = val[i];
    }
}

updateDate();

function updateVideo() {
    const btn = document.getElementById("btn_pause")
    const img = document.getElementById("cam0")
    img.src="/static/assets/noise.gif"
    btn.innerText = "StartVideo"
    btn.value = "0"
}

function pauseFunction() {
    const btn = document.getElementById("btn_pause")
    const img = document.getElementById("cam0")
    if (btn.value == "1") {
        console.log("BUTTONCLICK, pausing....");
        btn.value = "0"
        btn.innerText = "StartVideo"
        img.src = "/static/assets/noise.gif"
    }
    else {
        btn.value = "1"
        btn.innerText = "PauseVideo"
        console.log("Button play clicked!");
        img.src = "/video"
    }
}