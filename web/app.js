var buttons = [];

buttons.push({
  name: "Valgus 1 ",
  id: "lap_esimene_lamp",
});

buttons.push({
  name: "Valgus 2 ",
  id: "lap_teine_lamp",
});
buttons.push({
  name: "Valgus 3 ",
  id: "lap_kolmas_lamp",
});

function changeLED(light, state){
  var socket = new WebSocket("ws://iot.wut.ee/ws/" + light)
  socket.onopen = function(){
    socket.send(state)
	console.log(light + state)
    socket.close()
  }

}

$(function(){
	var buttonHtml = ""

	for(var id = 0; id < buttons.length; id++){
		buttonHtml += `<p>${buttons[id].name}</p><label class="switch"><input class="button" data-button-id="${id}" type="checkbox"><span class="slider round"><span></label><br><br>`
	}

	$("#buttonsContainer").html(buttonHtml)  //document.getElementBy("buttonsContainer").innerHTML = buttonHtml;

	$(".button").on("change", function()
	{
		var id = $(this).data("button-id");
		var checked = this.checked ? 1 : 0;
		changeLED(buttons[id].name, checked);
	});
});
