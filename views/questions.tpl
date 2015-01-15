%include('header_init.tpl', heading='Treat attribute')
	<div id="select">
		<table class="table">
			<thead>
				<tr>
					<th>Attribute</th>
					<th>Method</th>
					<th>N° questionnaires answered</th>
					<th>Answer new questionnaire</th>
					<th>Calulate utility function</th>
				</tr>
			</thead>
			<tbody id="table_attributes">
			</tbody>
		</table>
            </div>

%include('header_end.tpl')
%include('js.tpl')

<script>
$(function() { 
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));

	// We fill the table
	for (var i=0; i < asses_session.attributes.length; i++){
		var text = '<tr><td>' + asses_session.attributes[i].name + '</td><td>'+ asses_session.attributes[i].method + '</td><td>'+ asses_session.attributes[i].questionnaire.number +'</td>';
		if (asses_session.attributes[i].questionnaire.number < 3 && asses_session.attributes[i].completed == 'False') {
			text += '<td><button type="button" class="btn btn-default btn-xs answer_quest" id="q_' + asses_session.attributes[i].name  + '">Answer</button></td>';
		}
		else {
			text += '<td>Done</td>';
		}
		if (asses_session.attributes[i].completed == 'False'  && asses_session.attributes[i].questionnaire.number > 0) {
			text += '<td><button type="button" class="btn btn-default btn-xs calc_util" id="u_' + asses_session.attributes[i].name  + '">Utility function</button></td>';
		}
		else {
			text += '<td>Please answer questionnaire</td>';
		}
		$('#table_attributes').append(text);
	}


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////// CLICK ON THE ANSWER BUTTON //////////////////////////////////////////////////////////////// 
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	$('.answer_quest').click(function() {
		// we store the name of the attribute
		var name = $(this).attr('id').slice(2);

		// we delete the slect div
		$('#select').hide();

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

		//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		///////////////////////////////////////////////////////////////// PE METHOD //////////////////////////////////////////////////////////////// 
		//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		if (method == 'PE') {

			// VARIABLES
			var probability = 0.75;
			var min_interval = 0;
			var max_interval = 1;

			// INTERFACE

			$('.container-fluid').append(
				'<div id=\"choice\">\
			            	<img src="{{ get_url('static', path='img/tree_choice.png') }}" class="center"></img>\
			            	<span id="questions_val_min"></span>\
			            	<span id="questions_val_max"></span>\
			            	<span id="questions_val_mean"></span>\
			            	<span id="questions_proba_haut"></span>\
			            	<span id="questions_proba_bas"></span>\
			        	</div>'
			);
			$('#questions_val_min').append(val_min);
			$('#questions_val_max').append(val_max);

			// The certain gain will change whether it is the 1st, 2nd or 3rd questionnaire
			if (asses_session.attributes[indice].questionnaire.number == 0) {
				var gain_certain = parseFloat(val_min) + (parseFloat(val_max)+ parseFloat(val_min)) / 2;
				$('#questions_val_mean').append(gain_certain);
			}
			else if (asses_session.attributes[indice].questionnaire.number == 1) {
				var gain_certain = parseFloat(val_min) + (parseFloat(val_max)+ parseFloat(val_min)) / 4;
				$('#questions_val_mean').append(gain_certain);
			}
			else if (asses_session.attributes[indice].questionnaire.number == 2) {
				var gain_certain = parseFloat(val_min) + (parseFloat(val_max)+ parseFloat(val_min)) * 3 / 4;
				$('#questions_val_mean').append(gain_certain);
			}
			$('#choice').append('</div><button type="button" class="btn btn-default"><a id="gain">Gain</a></button><button type="button" class="btn btn-default"><a id="lottery">Lottery</a></button>');

			// FUNCTIONS
			function sync_values() {
				$('#questions_proba_haut').empty();
				$('#questions_proba_bas').empty();
				var proba_bas = 1 - probability;
				$('#questions_proba_bas').append(proba_bas.toFixed(2));
				$('#questions_proba_haut').append(probability);

			}

			function treat_answer(type, data){
				min_interval = data.interval[0];
				max_interval = data.interval[1];
				probability = parseFloat(data.proba).toFixed(2);

				if (max_interval - min_interval <= 0.05){
					sync_values();
					ask_final_value();
				}
				else {
					sync_values();
				}
			}

			function ask_final_value(){
				// we delete the choice div
				$('.btn').hide();
				$('.container-fluid').append(
					'<div id= "final_value" style="text-align: center;"><br /><br /><p>We are almost done, please now enter the value of the probability: <br /> '+ min_interval +'\
					 <= <input type="text" class="form-control" id="final_proba" placeholder="Probability" style="width: 100px; display: inline-block"> <= '+ max_interval +'</p><button type="button" class="btn btn-default final_validation">Validate</button></div>'
				);

				// when the user validate
				$('.final_validation').click(function(){
					var final_proba = parseFloat($('#final_proba').val());

					if (final_proba <= max_interval && final_proba >= min_interval) {
						// we save it 
						asses_session.attributes[indice].questionnaire.points.push([gain_certain, final_proba]);
						asses_session.attributes[indice].questionnaire.number += 1;
						// backup local
						localStorage.setItem("asses_session", JSON.stringify(asses_session));
						// we reload the page
						window.location.reload();
					}
				});
			}

			sync_values();

			// HANDLE USERS ACTIONS
			$('#gain').click(function() {
				$.post('ajax', '{"type":"question", "method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "0"}', function(data) {
					treat_answer('gain', data);
				});
			});

			$('#lottery').click(function() {
				$.post('ajax', '{"type":"question","method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "1"}', function(data) {
					treat_answer('lottery', data);
				});
			});
		}
	});

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////// CLICK ON THE UTILITY BUTTON //////////////////////////////////////////////////////////////// 
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	$('.calc_util').click(function() {
		// we store the name of the attribute
		var name = $(this).attr('id').slice(2);

		// we delete the slect div
		$('#select').hide();

		// which index is it ?
		var indice;
		for (var j = 0; j < asses_session.attributes.length; j++) {
			if(asses_session.attributes[j].name == name){
				indice = j;
			}
		}

		var val_min = asses_session.attributes[indice].val_min;
		var val_max = asses_session.attributes[indice].val_max;

		var points = asses_session.attributes[indice].questionnaire.points;
		points.push([val_max, 1]);
		points.push([val_max, 0]);
		json_2_send = {"type":"calc_util","method": "PE"};
		json_2_send["points"] = points;

		$.post('ajax', JSON.stringify(json_2_send), function(data) {
			console.log(data);
		});

	});
});
</script>

</body>

</html>
