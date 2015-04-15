%include('header_init.tpl', heading='K calculus')

<div role="tabpanel">
<!-- Nav tabs -->
<ul class="nav nav-tabs" role="tablist" >
  <li role="presentation" class="active"><a href="#multiplicative" aria-controls="multiplicative" role="tab" data-toggle="tab">Multiplicative</a></li>
  <li role="presentation"><a href="#multilinear" aria-controls="multilinear" role="tab" data-toggle="tab">Multilinear</a></li>

</ul>


 <!-- Tab panes -->
  <div class="tab-content">

    <div role="tabpanel" class="tab-pane active" id="multiplicative">
    	<table class="table">
			<thead>
				<tr>
					<th>Attribute</th>
					<th>Method</th>
					<th>Unit</th>
					<th>Utility function type</th>
                    <th>K</th>
                    <th><img src='/static/img/delete.ico' style='width:16px;'/></th>
				</tr>
			</thead>
			<tbody id="table_attributes">
			</tbody>
		</table>

<br />

	<div id="error_message">
	</div>
	<div id="k_calculus_info">
	</div>
            <div id="trees">
            </div>	
    </div>
    
    
     <!-- Panel for multiplicatif ! -->
    <div role="tabpanel" class="tab-pane" id="multilinear">
    <br/>
    	<table class="table">
			<thead>
				<tr>
					<th>Attribute</th>
					<th>Method</th>
					<th>Unit</th>
					<th>Utility function type</th> 
				</tr>
			</thead>
			<tbody id="table_attributes_multiplicatif">
			</tbody>
		</table>
    </div> 
  </div>
  <div style="float:left;width:100%;height:50px;"></div>
</div>

%include('header_end.tpl')
%include('js.tpl')

<script> var tree_image = '{{ get_url("static", path="img/tree_choice.png") }}'; </script>

<!-- Tree object -->
<script src="{{ get_url('static', path='js/tree.js') }}"></script>

<script>
$(function() { 
	$('li.k').addClass("active");
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));

	function isInArray(value, array) {
		return array.indexOf(value) > -1;
	}
	
	// We Check the requirements
	var req_nq = 0;
	var req_done = true;
	for (var i=0; i < asses_session.attributes.length; i++){
		var attribute = asses_session.attributes[i];
		if (attribute.completed == 'False') {
			req_done = false;
		}
		
		req_nq += 1;
	}


	//We display all the attribute in order to select wich one we want
	
	$('li.questions').addClass("active");
	$('#charts').hide();
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	//informations about the k already calculated
    var k_calculus = asses_session['k_calculus'];
	var nb_quest = k_calculus.nb_quest;
	var numeroK=0;
	// We fill the table
	for (var i=0; i < asses_session.attributes.length; i++){
		//If the utility fonction is not calculated we pass to the next one
		if(asses_session.attributes[i].completed == 'False')
			continue;
			
		
		var text = '<tr><td>' + asses_session.attributes[i].name + '</td>';
			text += '<td>'+ asses_session.attributes[i].method + '</td>';
			text += '<td>'+ asses_session.attributes[i].unit +'</td>';
			text += '<td>'+ asses_session.attributes[i].questionnaire.utilityType + '</td>';
			if(nb_quest>0 && typeof k_calculus.k[numeroK] != 'undefined') 
				text += '<td>'+ k_calculus.k[numeroK] + '</td>'; 
			else
				text += '<td>not calculated</td>'; 
			text+='<td><img id="deleteK'+numeroK+'" src="/static/img/delete.ico" style="width:16px;"/></td></tr>';
	
			$('#table_attributes').append(text);
			
		var text_multiplicatif = '<tr><td>' + asses_session.attributes[i].name + '</td>';
			text_multiplicatif += '<td>'+ asses_session.attributes[i].method + '</td>';
			text_multiplicatif += '<td>'+ asses_session.attributes[i].unit +'</td>'; 
			text_multiplicatif += '<td>'+ asses_session.attributes[i].questionnaire.utilityType + '</td>';
			$('#table_attributes_multiplicatif').append(text_multiplicatif);
			
			
			//we define the actions relatve of the delete img
			(function(_numeroK){
			$('#deleteK'+_numeroK).click(function(){ 
				asses_session['k_calculus']['k']=[]; 
				asses_session['k_calculus'].nb_quest=0;
				// backup local
				localStorage.setItem("asses_session", JSON.stringify(asses_session));
				//refresh the page
				window.location.reload();
				});
			})(numeroK);
			
			numeroK++;
	}

	
	
	


	
	if (req_nq < 3) {
		$('#error_message').append('<p>Error: In order to complete this task, you should have at least 3 attributes, please delete some</p>');
	}

	else if (!req_done) {
		$('#error_message').append('<p>Error: You should determine a utility function for each attribute before starting this task</p>');
	}

	else {
		// We check whether the user completed the first/second/third questionnaire
		var k_calculus = asses_session['k_calculus'];
		var nb_quest = k_calculus.nb_quest;

		if (nb_quest < req_nq ) {
			$('#k_calculus_info').append('<p>You have completed ' + nb_quest + ' / '+req_nq+' questionnaire(s)</p><br /><button type="button" class="btn btn-default answer_quest">Answer Next questionnaire</button>');
		}

		else {
			$('#k_calculus_info').append('<p>Process completed !</p>');
			// we check if the calculus has already been made :
			if (!isInArray('k_calculated', Object.keys(asses_session['k_calculus']))) {
				var list_temp = [0,0,0];
  
				for (var i = 0; i < asses_session['k_calculus']['k'].length; i++) {
					list_temp[i] = asses_session['k_calculus']['k'][i];
				}

				$.post('ajax', '{"type":"k_calculus", "k1": '+ list_temp[0] + ', "k2": '+ list_temp[1]+ ', "k3": '+ list_temp[2] +'}', function(data) {
					asses_session['k_calculus']['k_calculated'] = data.k;
					// backup local
					localStorage.setItem("asses_session", JSON.stringify(asses_session));
				});
			}

			var text_k = ''; 
			
			text_k += '<h4>K = ' + asses_session['k_calculus']['k_calculated']+'</h4>';

			$('#k_calculus_info').append(text_k);
		}
	}


//select the different view

	$('#multilinear').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
	})
	
	$('#multiplicatif a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
	})
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////// CLICK ON THE ANSWER BUTTON //////////////////////////////////////////////////////////////// 
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


  
	$('.answer_quest').click(function() {
		// we store the name of the attribute
		var method = 'PE';
		var numero_quest = nb_quest;
		var nb_attributs = req_nq;
		var mode = "normal";

		// we delete the slect div
		$('#k_calculus_info').hide();


		function random_proba(proba1, proba2) {
			var coin = Math.round(Math.random());
			if (coin == 1) {
				return proba1;
			}
			else {
				return proba2;
			}
		}

		//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		///////////////////////////////////////////////////////////////// PE METHOD //////////////////////////////////////////////////////////////// 
		//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		if (method == 'PE') {
			(function(){

				var probability = random_proba(0.25, 0.75);
				var min_interval = 0;
				var max_interval = 1;
				
				// VARIABLES
				var gain_certain = asses_session.attributes[numero_quest].val_max + ' ' + asses_session.attributes[numero_quest].unit;
				var gain_haut = asses_session.attributes[numero_quest].val_max + ' ' + asses_session.attributes[numero_quest].unit;
				var gain_bas = asses_session.attributes[numero_quest].val_min + ' ' + asses_session.attributes[numero_quest].unit;

				for (var i = 0; i < numero_quest; i++){
					gain_certain += ' <br/> ' + asses_session.attributes[i].val_min + ' ' + asses_session.attributes[i].unit;
					gain_haut += ' <br/> ' + asses_session.attributes[i].val_max + ' ' + asses_session.attributes[i].unit;
					gain_bas += ' <br/> ' + asses_session.attributes[i].val_min + ' ' + asses_session.attributes[i].unit;

				}

				for (var i = numero_quest + 1 ; i < nb_attributs; i++){
					gain_certain += ' <br/> ' + asses_session.attributes[i].val_min + ' ' + asses_session.attributes[i].unit;
					gain_haut += ' <br/> ' + asses_session.attributes[i].val_max + ' ' + asses_session.attributes[i].unit;
					gain_bas += ' <br/> ' + asses_session.attributes[i].val_min + ' ' + asses_session.attributes[i].unit;

				}

				// INTERFACE
				var arbre_gauche = new Arbre('gauche', '#trees');

				// SETUP ARBRE GAUCHE
				arbre_gauche.questions_proba_haut = probability;
				arbre_gauche.questions_val_max = gain_haut;
				arbre_gauche.questions_val_min = gain_bas;
				arbre_gauche.questions_val_mean = gain_certain;
				arbre_gauche.display();
				arbre_gauche.update();
				
				$('#trees').append('<br/><br/><br/><br/><button type="button" class="btn btn-default gain">Gain with certainty</button><button type="button" class="btn btn-default lottery">Lottery</button>');


				function treat_answer(data){
					min_interval = data.interval[0];
					max_interval = data.interval[1];
					probability = parseFloat(data.proba).toFixed(2);

					if (max_interval - min_interval <= 0.05){
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
						ask_final_value();
					}
					else {
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
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
							
							
							asses_session['k_calculus']['k'].push(final_proba);
								
							asses_session['k_calculus']['nb_quest']+= 1;
							// backup local
							localStorage.setItem("asses_session", JSON.stringify(asses_session));
							// we reload the page
							window.location.reload();
						}
					});
				}

				// HANDLE USERS ACTIONS
				$('.gain').click(function() {
					$.post('ajax', '{"type":"question", "method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "0", "mode": "'+String(mode)+'"}', function(data) {
						treat_answer(data);
					});
				});

				$('.lottery').click(function() {
					$.post('ajax', '{"type":"question","method": "PE", "proba": '+ String(probability) + ', "min_interval": '+ min_interval+ ', "max_interval": '+ max_interval+' ,"choice": "1" , "mode": "'+String(mode)+'"}', function(data) {
						treat_answer(data);
					});
				});
			})()
		}

	});
});
</script>

</body>

</html>
