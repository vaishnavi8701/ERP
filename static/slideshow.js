var myImage = document.getElementById("photo");
var imageArray = ["download1.jpg", "download2.jpg", "download3.jpg", "download4.jpg", "download5.jpg"];
var imageIndex = 0;

function changeImage() {
    photo.setAttribute("src", imageArray[imageIndex]);
    imageIndex++;
    if (imageIndex >= imageArray.length) {
        imageIndex = 0;
    }
}

var imageHandle = setInterval(changeImage, 2000);
photo.onclick = function() {
    clearInterval(imageHandle);
}