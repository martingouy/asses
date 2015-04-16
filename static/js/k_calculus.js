////////////////////////////////////////////////////////////////////////////////////////////////////////
///			javascript Function for k_calculus
////////////////////////////////////////////////////////////////////////////////////////////////////////

function checked_button_clicked(element)
{ 
	var checked=$(element).prop("checked");
	var i=$(element).val();
	
	//we modify the propriety
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	asses_session.attributes[i].checked=checked; 
	 
	//we update the assess_session storage 
	localStorage.setItem("asses_session", JSON.stringify(asses_session));
	
	//update
	update_checked_button();
}


function update_checked_button()
{
	var counter=number_attributes_checked();
	$("#message").html("You have selected "+counter+" attributes");
}

function number_attributes_checked()
{
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	var counter=0;
	for (var i=0; i < asses_session.attributes.length; i++){
		if(asses_session.attributes[i].checked)
			counter++;
	}
	
	return counter;
}

function update_method_button(type)
{
	//we modify the propriety
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	for(var i=0; i<asses_session.k_calculus.length; i++)
	{
		
		if(asses_session.k_calculus[i].method==type)
		{ 
			//we change also the look of the button of the current page 
			//we pass from gray to blue (default to primary)
			$("#button_"+type).removeClass('btn-default');
			$("#button_"+type).addClass('btn-primary'); 
 
			asses_session.k_calculus[i].active=true;
		}
		else
		{ 
			//we pass from blue to gray
			$("#button_"+asses_session.k_calculus[i].method).removeClass('btn-primary');
			$("#button_"+asses_session.k_calculus[i].method).addClass('btn-default'); 
			asses_session.k_calculus[i].active=false;
		}
	} 
	 
	//we update the assess_session storage 
	localStorage.setItem("asses_session", JSON.stringify(asses_session));
	
	 
}


///  ACTION FROM BUTTON MULTIPLICATIVE 
$("#button_multiplicative").click(function(){
	//update the active methode for k_kalculus
	update_method_button("multiplicative");
	create_multiplicative_k();
	update_k_list(0);
	show_list();
});

function create_multiplicative_k()
{
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	asses_session.k_calculus[0].k=[];
	var counter=1;
	//first we delete the array of k for multiplicative
	for (var i=0; i < asses_session.attributes.length; i++){
		if(asses_session.attributes[i].checked)
		{
			asses_session.k_calculus[0].k.push({"ID":counter, "ID_attribute":i, "attribute":asses_session.attributes[i].name, "value":null});
			counter++;
		}
	}
	//we update the assess_session storage 
	localStorage.setItem("asses_session", JSON.stringify(asses_session));
}



///  ACTION FROM BUTTON MULTILINEAR
$("#button_multilinear").click(function(){
	//update the active methode for k_kalculus
	update_method_button("multilinear");
	create_multilinear_k();
	update_k_list(1);
	show_list();
});	

function generer_list_lvl_0(n)
{
	var maList=[];
	for(var l=1; l<=n; l++)
		maList.push([l]);
	return maList;
}

function generer_list_1(i,n)
{
	var maList=[];
	for(var l=i; l<=n; l++)
		maList.push(l);
	return maList;
}

function generer_list(list_inf, n, lvl)
{
	if(lvl>=n)
		return [];
		
	var nouvelle_list = [];
	for(var i=0; i<list_inf.length; i++)
	{
		var list_1=generer_list_1(list_inf[i][list_inf[i].length-1]+1,n);
		for(var l=0; l<list_1.length; l++)
		{
			nouvelle_list.push(list_inf[i].concat(list_1[l]));
		}
		//nouvelle_list.push(new Array(list_inf[i][list_inf[i].length-1],)); 
	}
	
	return list_inf.concat(generer_list(nouvelle_list, n, lvl+1)); 
}


function create_multilinear_k()
{
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	asses_session.k_calculus[1].k=[];

	var checkedAttributeList=[];
	//first we delete the array of k for multiplicative
	for (var i=0; i < asses_session.attributes.length; i++){
		if(asses_session.attributes[i].checked)
			checkedAttributeList.push(i);
	}
	
	var maListeCombinaison=generer_list(generer_list_lvl_0(checkedAttributeList.length),checkedAttributeList.length, 0);
	
	
	for (var i=0; i < maListeCombinaison.length; i++){
		var id_attribute=[];
		var attribute=[];
		for(var j=0; j<maListeCombinaison[i].length; j++)
		{
			id_attribute.push(checkedAttributeList[maListeCombinaison[i][j]-1]);
			attribute.push(asses_session.attributes[checkedAttributeList[maListeCombinaison[i][j]-1]].name);
		}
		maListeCombinaison[i]
		asses_session.k_calculus[1].k.push({"ID":maListeCombinaison[i].join(), "ID_attribute":id_attribute, "attribute":attribute, "value":null});
	}
	
	//we update the assess_session storage 
	localStorage.setItem("asses_session", JSON.stringify(asses_session));
}




//// COMMUN FUNCTION FOR THE 2 METHODS
function update_k_list(number)
{
	
	//we delete the entire table
	$('#table_k_attributes').html("");
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
	var ma_list=asses_session.k_calculus[number].k; 
	
	for(var i=0; i<ma_list.length; i++)
	{
		var text = '<tr id="line'+i+'"><td>' + ma_list[i].ID + '</td>';
			text += '<td>'+ JSON.stringify(ma_list[i].attribute).replace(/"/g, ' ').replace("[", '').replace("]", ''); + '</td>';
			if(ma_list[i].value==null)
				text += '<td id="k_value_'+i+'"><button type="button" class="btn btn-default btn-xs" id="k_answer_'+i+'">Answer</button></td>';
			else
				text += '<td>'+ ma_list[i].value +'</td>';
				
			text+='<td><img id="delete_K'+i+'" src="/static/img/delete.ico" style="width:16px;"/></td></tr>';
					
			
			$('#table_k_attributes').append(text);
			
			if(ma_list[i].value==null)
			{
			(function(_i){
					$('#k_answer_'+_i).click(function(){ 
						$('#k_answer_'+_i).hide();
						if(number==0)//multiplicative
						k_answer(_i, number);
						else if(number==1)//multilinear
						k_multilinear_answer(_i, number);
					});
			})(i); 
			}
			
			(function(_i){
					$('#delete_K'+_i).click(function(){  
						asses_session.k_calculus[number].k[_i].value=null; 
						// backup local
						localStorage.setItem("asses_session", JSON.stringify(asses_session));
						//refresh the list
						update_k_list(number);
						});
					})(i);
				
	}
}

function show_list()
{
	$("#k_list").fadeIn(500);
}


function k_multilinear_answer(i)
{
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
		
			// we store the name of the attribute
		var method = 'PE';
		var mon_k = asses_session.k_calculus[1].k[i]; 
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
				var gain_certain = asses_session.attributes[mon_k.ID_attribute[0]].val_max + ' ' + asses_session.attributes[mon_k.ID_attribute[0]].unit;
				var gain_haut = asses_session.attributes[mon_k.ID_attribute[0]].val_max + ' ' + asses_session.attributes[mon_k.ID_attribute[0]].unit;
				var gain_bas = asses_session.attributes[mon_k.ID_attribute[0]].val_min + ' ' + asses_session.attributes[mon_k.ID_attribute[0]].unit;
				
				for (var l = 1; l < mon_k.ID_attribute.length; l++){
					var id = mon_k.ID_attribute[l];
					gain_certain += ' <br/> ' + asses_session.attributes[id].val_min + ' ' + asses_session.attributes[id].unit;
					gain_haut += ' <br/> ' + asses_session.attributes[id].val_max + ' ' + asses_session.attributes[id].unit;
					gain_bas += ' <br/> ' + asses_session.attributes[id].val_min + ' ' + asses_session.attributes[id].unit;

				}

				// INTERFACE
				//on cache le bouton
				$("#k_value_"+i).hide();
				$("#k_value_"+i).append("<br/><br/>");
				var arbre_gauche = new Arbre('gauche', "#k_value_"+i);

				// SETUP ARBRE GAUCHE
				arbre_gauche.questions_proba_haut = probability;
				arbre_gauche.questions_val_max = gain_haut;
				arbre_gauche.questions_val_min = gain_bas;
				arbre_gauche.questions_val_mean = gain_certain;
				arbre_gauche.display();
				arbre_gauche.update();
				
				$("#k_value_"+i).append('<br/><br/><br/><br/><button type="button" class="btn btn-default gain">Gain with certainty</button><button type="button" class="btn btn-default lottery">Lottery</button><br/><br/><div ></div>');
				//on affiche l'arbre avec un petit effet !
				
				$("#k_value_"+i).show("fast");

				function treat_answer(data){
					min_interval = data.interval[0];
					max_interval = data.interval[1];
					probability = parseFloat(data.proba).toFixed(2);

					if (max_interval - min_interval <= 0.05){
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
						ask_final_value(Math.round((max_interval + min_interval)*100/2)/100);
					}
					else {
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
					}
				}

				function ask_final_value(val){
					// we delete the choice div
					$('.gain').hide();$('.lottery').hide();
					$("#k_value_"+i).append(
						'<div id= "final_value" style="text-align: center;"><br /><br /><p>We are almost done, please now enter the value of the probability: <br /> '+ min_interval +'\
						 <= <input type="text" class="form-control" id="final_proba" placeholder="Probability" value="'+val+'" style="width: 100px; display: inline-block"> <= '+ max_interval +'</p><button type="button" class="btn btn-default final_validation">Validate</button></div>'
					);

					// when the user validate
					$('.final_validation').click(function(){
						var final_proba = parseFloat($('#final_proba').val());

						if (final_proba <= 1 && final_proba >= 0) {
							// we save it 
							asses_session.k_calculus[1].k[i].value=final_proba; //for multilinear it's 1
							// backup local 
							localStorage.setItem("asses_session", JSON.stringify(asses_session));
							// we reload the list
							$("#k_value_"+i).hide( "fast",function(){
								update_k_list(1);
							show_list();
							});
							 
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
}

function k_answer(i, type)
{ 
	 	var asses_session = JSON.parse(localStorage.getItem("asses_session"));
		
			// we store the name of the attribute
		var method = 'PE';
		var mon_k = asses_session.k_calculus[type].k[i];
		alert(JSON.stringify(mon_k));
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
				var gain_certain = asses_session.attributes[mon_k.ID_attribute].val_max + ' ' + asses_session.attributes[mon_k.ID_attribute].unit;
				var gain_haut = asses_session.attributes[mon_k.ID_attribute].val_max + ' ' + asses_session.attributes[mon_k.ID_attribute].unit;
				var gain_bas = asses_session.attributes[mon_k.ID_attribute].val_min + ' ' + asses_session.attributes[mon_k.ID_attribute].unit;
				
				for (var l = 0; l < i; l++){
					var pre_k = asses_session.k_calculus[type].k[l];
					gain_certain += ' <br/> ' + asses_session.attributes[pre_k.ID_attribute].val_min + ' ' + asses_session.attributes[pre_k.ID_attribute].unit;
					gain_haut += ' <br/> ' + asses_session.attributes[pre_k.ID_attribute].val_max + ' ' + asses_session.attributes[pre_k.ID_attribute].unit;
					gain_bas += ' <br/> ' + asses_session.attributes[pre_k.ID_attribute].val_min + ' ' + asses_session.attributes[pre_k.ID_attribute].unit;

				}

				for (var l = i + 1 ; l < asses_session.k_calculus[type].k.length; l++){
					var post_k = asses_session.k_calculus[type].k[l];
					gain_certain += ' <br/> ' + asses_session.attributes[post_k.ID_attribute].val_min + ' ' + asses_session.attributes[post_k.ID_attribute].unit;
					gain_haut += ' <br/> ' + asses_session.attributes[post_k.ID_attribute].val_max + ' ' + asses_session.attributes[post_k.ID_attribute].unit;
					gain_bas += ' <br/> ' + asses_session.attributes[post_k.ID_attribute].val_min + ' ' + asses_session.attributes[post_k.ID_attribute].unit;

				}

				// INTERFACE
				//on cache le bouton
				$("#k_value_"+i).hide();
				$("#k_value_"+i).append("<br/><br/>");
				var arbre_gauche = new Arbre('gauche', "#k_value_"+i);

				// SETUP ARBRE GAUCHE
				arbre_gauche.questions_proba_haut = probability;
				arbre_gauche.questions_val_max = gain_haut;
				arbre_gauche.questions_val_min = gain_bas;
				arbre_gauche.questions_val_mean = gain_certain;
				arbre_gauche.display();
				arbre_gauche.update();
				
				$("#k_value_"+i).append('<br/><br/><br/><br/><button type="button" class="btn btn-default gain">Gain with certainty</button><button type="button" class="btn btn-default lottery">Lottery</button><br/><br/><div ></div>');
				//on affiche l'arbre avec un petit effet !
				
				$("#k_value_"+i).show("fast");

				function treat_answer(data){
					min_interval = data.interval[0];
					max_interval = data.interval[1];
					probability = parseFloat(data.proba).toFixed(2);

					if (max_interval - min_interval <= 0.05){
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
						ask_final_value(Math.round((max_interval + min_interval)*100/2)/100);
					}
					else {
						arbre_gauche.questions_proba_haut = probability;
						arbre_gauche.update();
					}
				}

				function ask_final_value(val){
					// we delete the choice div
					$('.gain').hide();$('.lottery').hide();
					$("#k_value_"+i).append(
						'<div id= "final_value" style="text-align: center;"><br /><br /><p>We are almost done, please now enter the value of the probability: <br /> '+ min_interval +'\
						 <= <input type="text" class="form-control" id="final_proba" placeholder="Probability" value="'+val+'" style="width: 100px; display: inline-block"> <= '+ max_interval +'</p><button type="button" class="btn btn-default final_validation">Validate</button></div>'
					);

					// when the user validate
					$('.final_validation').click(function(){
						var final_proba = parseFloat($('#final_proba').val());

						if (final_proba <= 1 && final_proba >= 0) {
							// we save it 
							asses_session.k_calculus[type].k[i].value=final_proba; 
							// backup local 
							localStorage.setItem("asses_session", JSON.stringify(asses_session));
							// we reload the list
							$("#k_value_"+i).hide( "fast",function(){
								update_k_list(type);
							show_list();
							});
							 
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

}