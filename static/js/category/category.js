function getResponseForCategoryCreate() {
    getToasterMessage("success", "Category Created Successfully");
    setTimeout(function() {
    $("#createCategory").submit();
    }, 1000);
}

function getResponseForCategoryUpdate() {
    getToasterMessage("success", "Category Updated Successfully");
    setTimeout(function() {
    $("#updateCategory").submit();
    }, 1000);
}

function getResponseForCategoryDelete() {
    getToasterMessage("success", "Category Deleted Successfully");
    setTimeout(function() {
    $("#deleteCategory").submit();
    }, 1000);
}

function deleteUser(id) {
    $('#deleteModal').modal('show');
    $('#userId').val(id);
}

$("#deleteCategory").on("submit", function(event){
    event.preventDefault();
    var id = $('#userId').val();
    $('#deleteModal').modal('hide');
    $.ajax({
        url: '/category/delete/' + id + '/',
        type:'POST',
        dataType: 'json',
        headers: {
           'X-CSRFToken': csrf_token
         },
        data: {
            "id": id
        },
        success: function(result) {
            window.location.reload();
        }
    });
});
