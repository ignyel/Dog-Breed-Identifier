function upload(formData) {
    $("body").css("cursor", "wait");
    $.ajax({
        url: "/results",
        type: "post",
        processData: false,
        contentType: false,
        data: formData
    }).done(function (response) {
        $("#results").html(response);
        // Set this again, because the drop area was just replaced
        $(".droparea").on(dropHandlerSet);
        $("body").css("cursor", "default");
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(textStatus, errorThrown);
    });
}

function getDataAndUpload() {
    var formData = new FormData(document.querySelector('form'));
    upload(formData);
}

var dragHandler = function (evt) {
    evt.preventDefault();
};

var dropHandler = function (evt) {
    evt.preventDefault();
    var files = evt.originalEvent.dataTransfer.files;
    var file = files[0];
    var fileName = "";

    // Welcome to JavaScript!
    if ('name' in file) {
        fileName = file.name;
    }
    else {
        fileName = file.fileName;
    }

    var formData = new FormData();
    formData.append("input-photo", file, fileName);
    upload(formData);
};

var dropHandlerSet = {
    dragover: dragHandler,
    drop: dropHandler
};

$(".droparea").on(dropHandlerSet);
