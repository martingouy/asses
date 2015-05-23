





///  ACTION FROM BUTTON UPDATE
$(function() {

	$('li.export').addClass("active");
	$('#export_json').click(function() {
		var data_2_export = localStorage['asses_session'];
		var button  = $('#export_json');
		button.attr('href', 'data:attachment/json,' + data_2_export);
		button.attr('target', '_blank');
		button.attr('download', 'myFile.json');
	});

	$('#export_xls').click(function() {
		var data_2_export = localStorage['asses_session'];
		$.post('ajax', '{"type":"export_xls", "data":'+data_2_export+'}', function(data) {
			document.location = "export_download/"+data;
		});
	});


	list();
});


function reduce(nombre){return Math.round(nombre*1000000)/1000000;}
function signe(nombre){if(nombre>=0){return "+"+nombre}else{return nombre}};

function list()
{
	var asses_session = JSON.parse(localStorage.getItem("asses_session"));

	// We fill the table
	for (var i=0; i < asses_session.attributes.length; i++){
		if(!asses_session.attributes[i].checked)//if note activated
			continue;//we pass to the next one
		var text = '<tr><td>' + asses_session.attributes[i].name + '</td>';
		text+='<td>'+ asses_session.attributes[i].unit + '</td>';
		text+='<td id="charts_'+i+'"></td>';
		text+='<td id="functions_'+i+'"></td>';
		text+='</tr>';

		$('#table_attributes').append(text);

		(function(_i) {
			var json_2_send = {"type": "calc_util", "points":[]};
			var points = asses_session.attributes[_i].questionnaire.points.slice();
			var mode = asses_session.attributes[_i].mode;
			var val_max=asses_session.attributes[_i].val_max;
			var val_min=asses_session.attributes[_i].val_min;
			if (points.length > 0) {
			if (mode=="normal") {
				points.push([val_max, 1]);
				points.push([val_min, 0]);
			}
			else {
				points.push([val_max, 0]);
				points.push([val_min, 1]);
			}
			json_2_send["points"] = points;
				$.post('ajax', JSON.stringify(json_2_send), function (data) {
					$.post('ajax', JSON.stringify({
						"type": "svg",
						"data": data,
						"min": val_min,
						"max": val_max,
						"liste_cord": points,
						"width": 3
					}), function (data2) {

						$('#charts_' + _i).append('<div>' + data2 + '</div>');
						var functions="";
						for (var key in data) {
							$('#charts').show();
							if (key == 'exp')
								functions+='<label style="color:#401539"><input type="checkbox"> Exponential (' + Math.round(data[key]['r2'] * 100) / 100 + ')</label><br/>';
							else if (key == 'log')
								functions+='<label style="color:#D9585A"><input type="checkbox"> Logarithmic (' + Math.round(data[key]['r2'] * 100) / 100 + ')</label><br/>';
							else if (key == 'pow')
								functions+='<label style="color:#6DA63C"><input type="checkbox"> Power (' + Math.round(data[key]['r2'] * 100) / 100 + ')</label><br/>';
							else if (key == 'quad')
								functions+='<label style="color:#458C8C"><input type="checkbox"> Quadratic (' + Math.round(data[key]['r2'] * 100) / 100 + ')</label><br/>';
							else if (key == 'lin')
								functions+='<label style="color:#D9B504"><input type="checkbox"> Linear (' + Math.round(data[key]['r2'] * 100) / 100 + ')</label><br/>';
						}
						$('#functions_' + _i).append(functions);
					})
				});
			}
			else
			{
				$('#charts_' + _i).append("Please answer questionnaire first");
			}
		})(i);



	}
}