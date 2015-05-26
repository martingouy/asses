%include('header_init.tpl', heading='Multi Attributes')
<div class="page-header">
  <h3>Ki calculus</h3>
</div>

<div class="alert alert-info" role="alert" id="update_box" >
  
  <button type="button" class="btn btn-info" id="update"><span class="glyphicon glyphicon-refresh" aria-hidden="true"></span></button>
  <span id="update_attributes_number"></span> attributes are activated but <span id="update_k_number"></span> are used for K calculus. You need to refresh K list. All K value will be reseted.
</div>
        
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


<br/>
<div class="page-header">
  <h3>K calculus</h3>
</div>

<div class="alert alert-info" role="alert" id="calculatek_box_multiplicative" >
  You need to calculate all ki in order to calculate K.
</div>

<div class="alert alert-info" role="alert" id="calculatek_box_multilinear" >
  There is no need to calculate K in multilinear.
</div>

<div style="text-align:center;" id="GK">

	<span class="h4">K = <span id="GK_value"></span> </span><button type="button" class="btn btn-default btn-lg" id="button_calculate_k" style="text-align:center">Calculate</button>
	<br/>
</div>


<br/>
<div class="page-header">
  <h3>Choose utility function for each attributes</h3>
</div>
<div id="attribute" >
    <table class="table">
    <thead>
    <tr>
    <th>K</th>
    <th>Attribute</th>
    <th>Graph</th>
    <th>Function</th>
    </tr>
    </thead>
    <tbody id="table_attributes">
    </tbody>
    </table>
</div>


<div style="text-align:center;" id="button_generate_list">

	<button type="button" class="btn btn-default btn-lg" id="button_calculate_k" style="text-align:center">Generate list</button>
	<br/>
</div>


<div class="page-header">
  <h3>Calcul Utility function</h3>
</div>

<div style="text-align:center;" id="button_generate_list">

	<button type="button" class="btn btn-default btn-lg" id="button_calculate_utility" style="text-align:center">Calcul general utility function</button>
	<br/><br/>
	<span class="h4" id="utility_function"></span>
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
	
	



});
</script>

</body>

</html>
