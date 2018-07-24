function updateImage() {
  var input = document.getElementById("image_input");
  var file = input.files[0];
  var reader = new FileReader();
  reader.addEventListener('load', function (){
    console.log(reader.result);
    // document.getElementById("image_input").value = reader.result;
  });
  reader.readAsDataURL(file);
}

function submitForm() {

    //picture = document.getElementById("image_input").value
    college = document.getElementById("college").value
    size = document.getElementById("size").value
    console.log(college)
    // color = ndb.StringProperty(required=True)
    // neck_type = ndb.StringProperty(required=True)
    // sleeve_type = ndb.StringProperty(required=True)
    // picture = ndb.BlobProperty(required=True)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/upload", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "college" : college
    }));

}
