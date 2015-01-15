%include('header_init.tpl', heading='Treat attribute')
	<div id="select">
		<div class="form-group">
			<label for="select_attr">Method:</label>
			<select class="form-control" id="select_attr">
			</select>
		</div>
	            <button type="button" class="btn btn-default"><a id="start">Click to start</a></button>
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
			$('#questions_val_mean').append((parseFloat(val_max)+ parseFloat(val_min)) / 2);
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
				//$('#choice').remove();
				$('.btn').hide();
				$('.container-fluid').append(
					'<div id= "final_value" style="text-align: center;"><br /><br /><p>We are almost done, please now enter the value of the probability: <br /> '+ min_interval +'\
					 <= <input type="text" class="form-control" id="final_proba" placeholder="Probability" style="width: 100px; display: inline-block"> <= '+ max_interval +'</p><button type="button" class="btn btn-default">Validate</button></div>'

				);
			}

			sync_values();

			// HANDLE USERS ACTIONS
			$('#gain').click(function() {
				$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "0"}', function(data) {
					treat_answer('gain', data);
				});
			});

			$('#lottery').click(function() {
				$.post('ajax', '{"method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "1"}', function(data) {
					treat_answer('lottery', data);
				});
			});
		}
	});
});
</script>

</body>

</html>
