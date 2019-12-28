function MotorCtrl(message){
	var request = new XMLHttpRequest();
	request.open("GET", "http://「ラズパイのIP」:5000/" + message, true);
    request.send();
}
// ページ読込完了後にボタンにclickイベントを登録する
window.addEventListener("load", function(){
	document.getElementById("forward").addEventListener("click", function(){
	MotorCtrl("forward");
	}, false);
        document.getElementById("stop").addEventListener("click", function(){
        MotorCtrl("stop");
        }, false);
        document.getElementById("back").addEventListener("click", function(){
        MotorCtrl("back");
        }, false);
        document.getElementById("right").addEventListener("click", function(){
        MotorCtrl("right");
        }, false);
        document.getElementById("left").addEventListener("click", function(){
        MotorCtrl("left");
        }, false);
}, false);
