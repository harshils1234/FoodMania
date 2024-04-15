function getResponseForFoodUpdate(){
    getToasterMessage("success", "Food Updated Successfully");
    setTimeout(function() {
    $("#updateFood").submit();
    }, 1000);
}
