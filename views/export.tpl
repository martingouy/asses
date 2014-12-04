%include('header_init.tpl', heading='Export')

            <button type="button" class="btn btn-default"><a id="export_json">Click to export</a></button>

%include('header_end.tpl')
%include('js.tpl')

<script>
    $('li.export').addClass("active");
    $('#export_json').click(function() {
        var data_2_export = localStorage['asses_session'];
        var button  = $('#export_json');
        button.attr('href', 'data:attachment/json,' + data_2_export);
        button.attr('target', '_blank');
        button.attr('download', 'myFile.json');
    });
</script>

</body>

</html>
