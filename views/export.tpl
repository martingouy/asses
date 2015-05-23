%include('header_init.tpl', heading='Export')

<div class="page-header">
    <h3>export all</h3>
</div>

<button type="button" class="btn btn-default"><a id="export_xls">Click to export Excel</a></button><br/>

<div class="page-header">
    <h3>choose exportation</h3>
</div>

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



%include('header_end.tpl')
%include('js.tpl')
<script src="{{ get_url('static', path='js/export.js') }}"></script>>






</body>


</html>
