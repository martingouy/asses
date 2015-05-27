%include('header_init.tpl', heading='Export')

<div class="page-header">
    <h3>export all</h3>
</div>

<button type="button" class="btn btn-default" id="export_xls">Click to export Excel</button><br/>

<div class="page-header">
    <h3>choose your exportation in detail</h3>
</div>

<h4>Choose specific utility function for attribute</h4>
<div id="attribute" >
    <table class="table">
    <thead>
    <tr>
    <th>Attribute</th>
    <th>Unit</th>
    <th>Graph</th>
    <th>Function</th>
    </tr>
    </thead>
    <tbody id="table_attributes">
    </tbody>
    </table>
</div>

<br/>
<h4>Choose K</h4>

<label><input type="checkbox" id="checkbox_multilinear"> Multi-Attribut multilinearite</label><br/>
<label><input type="checkbox" id="checkbox_multiplicative"> Multi-Attribut multiplicatif</label><br/>
<br/>
<button type="button" class="btn btn-default" id="export_xls_option">Click to export in Excel</button><br/>


%include('header_end.tpl')
%include('js.tpl')
<script src="{{ get_url('static', path='js/export.js') }}"></script>>






</body>


</html>
