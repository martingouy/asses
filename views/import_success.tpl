%include('header_init.tpl', heading='Import Excel file')

<div class="alert alert-success" role="alert" id="calculatek_box" >
  File sucessfully imported
</div>


<form action="/upload" method="post" enctype="multipart/form-data">
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" name="upload">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>



	<form action="/upload" method="post" enctype="multipart/form-data">
      Select a file: <input type="file" name="upload" />
      <button type="submit" class="btn btn-default btn-lg">Import</button>
    </form>



%include('header_end.tpl')

%include('js.tpl')

<script type="text/javascript">
  $('li.import').addClass("active");
  function loadFile() {
    var input, file, fr;

    if (typeof window.FileReader !== 'function') {
      alert("The file API isn't supported on this browser yet.");
      return;
    }

    input = document.getElementById('fileinput');
    if (!input) {
      alert("Um, couldn't find the fileinput element.");
    }
    else if (!input.files) {
      alert("This browser doesn't seem to support the `files` property of file inputs.");
    }
    else if (!input.files[0]) {
      alert("Please select a file before clicking 'Load'");
    }
    else {
      file = input.files[0];
      fr = new FileReader();
      fr.onload = receivedText;
      fr.readAsText(file);
    }

    function receivedText(e) {
      lines = e.target.result;
      localStorage.setItem("asses_session", lines);
    }

    window.location.href = "attributes";
  }
</script>


</body>

</html>
