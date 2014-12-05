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
            </div>

%include('header_end.tpl')
%include('js.tpl')

<script>
$(function() { 
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

		$('#choice').append('val_min=' + val_min +'<br />val_max=' + val_max);
		$('#choice').append('<div id="proba">'+ String(probability) +'</div><button type="button" class="btn btn-default"><a id="gain">Gain</a></button><button type="button" class="btn btn-default"><a id="lottery">Lottery</a></button>');


		$('#gain').click(function() {
			$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "choice": "0"}', function(data) {
				probability = parseFloat(data);
				$('#proba').empty();
				$('#proba').append(probability);
			});
		});

		$('#lottery').click(function() {
			$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "choice": "1"}', function(data) {
				probability = parseFloat(data);
				$('#proba').empty();
				$('#proba').append(probability);
			});
		});
	});
});
</script>

</body>

</html>
