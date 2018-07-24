function updateImage() {
  var input = document.getElementById("image_input");
  var file = input.files[0];
  var reader = new FileReader();
  reader.addEventListener('load', function (){
    console.log(reader.result);
  });
  reader.readAsDataURL(file);
}
