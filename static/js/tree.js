////////////////////////////////////////////////////////////////////////////////////////////////////////
///				OBJET ARBRE
////////////////////////////////////////////////////////////////////////////////////////////////////////

var Arbre = function(id, target) {
	this.questions_val_min;
	this.questions_val_max;
	this.questions_val_mean;
	this.questions_proba_haut;
	this.div_target = target;
	this.identifiant = id;
	this.dislayed = false;
	this.html = 
	'<div class="proba_tree" id=\"tree_'+ this.identifiant +'\">\
            	<img src="'+ tree_image +'" class="center img_tree"></img>\
            	<span class="questions_val_min"></span>\
            	<span class="questions_val_max"></span>\
            	<span class="questions_val_mean"></span>\
            	<span class="questions_proba_haut"></span>\
            	<span class="questions_proba_bas"></span>\
        	</div>';
}

Arbre.prototype.display = function(){
	if (!this.dislayed && this.div_target) {
		// we append the html
		$(this.div_target).append(this.html);
		this.displayed = true;
	}
}

Arbre.prototype.remove = function(){
	if ( this.displayed) {
		$('#tree_' + this.identifiant).remove();
		this.displayed = false;
	}
}

Arbre.prototype.update = function(){
	$('#tree_' + this.identifiant+ ' .questions_val_min').empty();
	$('#tree_' + this.identifiant+ ' .questions_val_min').append(this.questions_val_min);
	$('#tree_' + this.identifiant+ ' .questions_val_max').empty();
	$('#tree_' + this.identifiant+ ' .questions_val_max').append(this.questions_val_max);
	$('#tree_' + this.identifiant+ ' .questions_val_mean').empty();
	$('#tree_' + this.identifiant+ ' .questions_val_mean').append(this.questions_val_mean);
	$('#tree_' + this.identifiant+ ' .questions_proba_haut').empty();
	$('#tree_' + this.identifiant+ ' .questions_proba_haut').append(this.questions_proba_haut);
	$('#tree_' + this.identifiant+ ' .questions_proba_bas').empty();
	$('#tree_' + this.identifiant+ ' .questions_proba_bas').append((1 - this.questions_proba_haut).toFixed(2));
}