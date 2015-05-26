%include('header_init.tpl', heading='Import Excel file')



<form action="/upload" method="post" enctype="multipart/form-data">
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" name="upload">
    <p class="help-block">Only xlsx files are supporter. Files must have the datas must have the same position as when we export xlsx files (position of attributes, points, ...).</p>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>



%include('header_end.tpl')

%include('js.tpl')




</body>

</html>
