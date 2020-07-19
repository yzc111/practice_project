
$(document).ready(function () {
    document.getElementById('name').value=localStorage.getItem("name");
});

//物品详情页面的加入购物车按钮
$(function(){
    $("#details_collect").click(function() {
        $.ajax({
            url: 'http://127.0.0.1:9090/book/saveBook',
            type: 'get',
            contentType: "application/json;charset=utf-8",
            dataType: 'json',
            data: {
                nam: $("#nam").val(),
                intro: $("#intro").val(),
                price: $("#price").val(),
                lag: $("#lag").val(),
                typ: $("#typ").val(),
                cond: $("#cond").val(),
                ctime: $("#ctime").val(),
                stock: $("#stock").val(),
                seller: $("#seller").val(),
                name: $("#name").val()
            },
            success: function (data) {
                alert("成功！")
            },
            error: function (response) {
                alert("失败！")
            }
        });
    })})