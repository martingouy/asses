%include('header_init.tpl', heading='Manage your attributes')

<br />
<br />
<h2 style="display:inline-block; margin-right: 40px;"> Delete current simulation: </h2>
<button type="button" class="btn btn-default del_simu">Delete</button>
<h2> List of current attributes: </h2>
<table class="table">
  <thead>
    <tr>
    <th>Attribut</th>
    <th>Unité</th>
    <th>Valeurs</th>
    <th>Méthode</th>
    <th>Etat</th>
    <th><img src='/static/img/delete.ico' style='width:16px;'/></th>
    </tr>
  </thead>
  <tbody id="table_attributes">
  </tbody>
</table>
<br />
<br />
<div id="add_attribute">
    <h2> Add a new attribute: </h2>

    <div class="form-group">
        <label for="att_name">Name:</label>
        <input type="text" class="form-control" id="att_name" placeholder="Name">
    </div>

    <div class="form-group">
        <label for="att_unit">Unit:</label>
        <input type="text" class="form-control" id="att_unit" placeholder="Unit">
    </div>
    <div class="form-group">
        <label for="att_value_min">Value Min:</label>
        <input type="text"  class="form-control" id="att_value_min" placeholder="Value">
    </div>
    <div class="form-group">
        <label for="att_value_max">Value Max:</label>
        <input type="text"  class="form-control" id="att_value_max" placeholder="Value">
    </div>
    <div class="form-group">
        <label for="att_method">Method:</label>
        <select class="form-control">
          <option>PE</option>
          <option>LE</option>
          <option>CE_Constant_Prob</option>
          <option>CE Variable Prob.</option>
        </select>
    </div>
    <div class="checkbox">
        <label>
          <input name="mode" type="checkbox"> The min value is optimal
        </label>
    </div>

    <button type="submit" class="btn btn-default" id="submit">Submit</button>
</div>


%include('header_end.tpl')

%include('js.tpl')
<script>
    $(function() {

       

        $('li.manage').addClass("active");
        var asses_session = JSON.parse(localStorage.getItem("asses_session"));

        
        if (!asses_session){
            asses_session = {"attributes": [], "k_calculus": {"nb_quest": 0, "k" :[]} };
            localStorage.setItem("asses_session", JSON.stringify(asses_session));
        }

        function sync_table() { 
			$('#table_attributes').empty();
            if (asses_session){
                for (var i=0; i < asses_session.attributes.length; i++) {
                    var attribute = asses_session.attributes[i];
                    var text_table = '<tr><td>'+ attribute.name +'</td><td>'+ attribute.unit +'</td><td>['+ attribute.val_min +','+ attribute.val_max +']</td><td>'+ attribute.method +'</td><td>'+ attribute.completed +'</td>';
					text_table+='<td><img id="deleteK'+i+'" src="/static/img/delete.ico" style="width:16px;"/></td></tr>';
					
					$('#table_attributes').append(text_table);
				
					(function(_i){
					$('#deleteK'+_i).click(function(){ 
						asses_session.attributes.splice(_i,1); 
						// backup local
						localStorage.setItem("asses_session", JSON.stringify(asses_session));
						//refresh the page
						window.location.reload();
						});
					})(i);
                }

            }
        }
        sync_table();

        var name = $('#att_name').val();

        $('#submit').click(function() {
            var name = $('#att_name').val();
            var unit = $('#att_unit').val();
            var val_min = parseInt($('#att_value_min').val());
            var val_max = parseInt($('#att_value_max').val());
            var method = $( "select option:selected" ).text();

            if( $('input[name=mode]').is(':checked') ) {
                var mode = "reversed";	
            }
            else {
                var mode = "normal";
            }

            if (!(name || unit || val_min || val_max) || isNaN(val_min) || isNaN(val_max)) {
                alert('Please fill correctly all the fields');
            }
            else {
                asses_session.attributes.push({"name": name, 'unit': unit, 'val_min': val_min, 'val_max': val_max, 'method': method, 'mode' : mode ,'completed': 'False', 'questionnaire': {'number': 0, 'points': [], 'utility': {}}});
                sync_table();
                localStorage.setItem("asses_session", JSON.stringify(asses_session));
            }
			
			
        });

        function isAttribute(name){
            for (var i=0; i < asses_session.attributes.length; i ++) {
                if (asses_session.attributes[i].name == name) {
                    return [true, i];
                }
            }
            return [false, 0];
        }

        
    });
</script>
</body>

</html>
