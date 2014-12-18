%include('header_init.tpl', heading='Treat attribute')
	<div id="select">
		<div class="form-group">
			<label for="select_attr">Method:</label>
			<select class="form-control" id="select_attr">
			</select>
		</div>
	            <button type="button" class="btn btn-default"><a id="start">Click to start</a></button>
            </div>
            <div id="choice">
            	<img src="{{ get_url('static', path='img/tree_choice.png') }}" class="center"></img>
            	<span id="questions_val_min"></span>
            	<span id="questions_val_max"></span>
            	<span id="questions_val_mean"></span>
            	<span id="questions_proba_haut"></span>
            	<span id="questions_proba_bas"></span>

            </div>

%include('header_end.tpl')
%include('js.tpl')

<script>
$(function() { 
	$('#choice').hide();
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));

	var text = ''
	for (var i=0; i < asses_session.attributes.length; i++){
		text += '<option>' + asses_session.attributes[i].name + '</option>';
	}
	$('#select_attr').append(text);

	$('li.export').addClass("questions");


	$('#start').click(function() {
		// we store the name of the attribute
		var name = $( "select option:selected" ).text();

		// we delete the slect div
		$('#select').remove();

		// we show the choice div
		$('#choice').show();

		// which index is it ?
		var indice;
		for (var j = 0; j < asses_session.attributes.length; j++) {
			if(asses_session.attributes[j].name == name){
				indice = j;
			}
		}

		var val_min = asses_session.attributes[indice].val_min;
		var val_max = asses_session.attributes[indice].val_max;
		var method = asses_session.attributes[indice].method;
		var probability = 0.5;

		$('#questions_val_min').append(val_min);
		$('#questions_val_max').append(val_max);
		$('#questions_val_mean').append((parseFloat(val_max)+ parseFloat(val_min)) / 2);
		$('#choice').append('</div><button type="button" class="btn btn-default"><a id="gain">Gain</a></button><button type="button" class="btn btn-default"><a id="lottery">Lottery</a></button>');

		function sync_values() {
			$('#questions_proba_haut').empty();
			$('#questions_proba_bas').empty();
			var proba_bas = 1 - probability;
			$('#questions_proba_bas').append(proba_bas.toFixed(2));
			$('#questions_proba_haut').append(probability);

		}

		sync_values();

		$('#gain').click(function() {
			$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "choice": "0"}', function(data) {
				if (Math.abs(probability - parseFloat(data).toFixed(2)) <= 0.05){
					alert('END!');
					probability = parseFloat(data).toFixed(2);
					sync_values();
				}
				else {
					probability = parseFloat(data).toFixed(2);
					sync_values();
				}
			});
		});

		$('#lottery').click(function() {
			$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "choice": "1"}', function(data) {
				if (Math.abs(probability - parseFloat(data).toFixed(2)) <= 0.05){
					alert('END!');
					probability = parseFloat(data).toFixed(2);
					sync_values();
				}
				else {
					probability = parseFloat(data).toFixed(2);
					sync_values();
				}
			});
		});
	});
});
</script>

</body>

</html>
