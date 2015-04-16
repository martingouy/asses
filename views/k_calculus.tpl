%include('header_init.tpl', heading='K calculus')

<table class="table">
			<thead>
				<tr>
					<th>Attribute</th>
					<th>Method</th>
					<th>Unit</th>
					<th>Utility function type</th> 
                    <th>check</th>
				</tr>
			</thead>
			<tbody id="table_attributes">
			</tbody>
		</table>
        
<div id="error_message">
	</div>
    <div id="message">
	</div>
    
    <div id="button_method" style="text-align:center;">
    <button type="button" class="btn btn-default btn-lg" id="button_multiplicative">Multiplicative</button>
    <button type="button" class="btn btn-default btn-lg" id="button_multilinear">Multilinear</button>
	</div>
<div id="k_list" style="display:none">
<table class="table">
		<thead>
			<tr>
				<th>K</th>
				<th>Relative Attribute</th>
				<th>Value</th>  
                <th><img src="/static/img/delete.ico" style="width:16px;"/></th>
			</tr>
		</thead>
		<tbody id="table_k_attributes">
		</tbody>
</table>
</div>

<div id="k_calculus_info">
	</div>
<div id="trees">
</div>	



%include('header_end.tpl')
%include('js.tpl')

<script> var tree_image = '{{ get_url("static", path="img/tree_choice.png") }}'; </script>

<!-- Tree object -->
<script src="{{ get_url('static', path='js/tree.js') }}"></script>
<script src="{{ get_url('static', path='js/k_calculus.js') }}"></script>

<script>
$(function() { 
	$('li.k').addClass("active");
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));

	function isInArray(value, array) {
		return array.indexOf(value) > -1;
	}
	
	//we toggle the button we used
	for(var i=0; i<asses_session.k_calculus.length; i++)
	{ 
		if(asses_session.k_calculus[i].active==true)
		{
			$("#button_"+asses_session.k_calculus[i].method).removeClass('btn-default');
			$("#button_"+asses_session.k_calculus[i].method).addClass('btn-primary'); 
			update_k_list(i);
			show_list();
		}
		else
		{
			$("#button_"+asses_session.k_calculus[i].method).removeClass('btn-primary');
			$("#button_"+asses_session.k_calculus[i].method).addClass('btn-default'); 
		}
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
		
		
		var text = '<tr><td>' + asses_session.attributes[i].name + '</td>';
			text += '<td>'+ asses_session.attributes[i].method + '</td>';
			text += '<td>'+ asses_session.attributes[i].unit +'</td>';
			text += '<td>'+ asses_session.attributes[i].questionnaire.utilityType + '</td>';
			
			if(asses_session.attributes[i].checked)
			text+='<td><input type="checkbox" id="checkbox_'+i+'" value="'+i+'" name="' + asses_session.attributes[i].name + '" checked></td></tr>';
			else
			text+='<td><input type="checkbox" id="checkbox_'+i+'" value="'+i+'" name="' + asses_session.attributes[i].name + '" ></td></tr>';
			
			$('#table_attributes').append(text);
			
			//we will define the action when we click on the check input
			$('#checkbox_'+i).click(function(){checked_button_clicked($(this))});
			
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

	
	
	
/*
	
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
*/

//select the different view

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////// CLICK ON THE ANSWER BUTTON //////////////////////////////////////////////////////////////// 
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



});
</script>

</body>

</html>
