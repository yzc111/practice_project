//个人中心模块的根目录栏
$(document).ready(function () {
	$.ajax({
		type: "get",
		url: "http://127.0.0.1:9090/book/findByUid",
		dataType: "json",
        data:{name:localStorage.getItem("name")},
		success: function (data) {
            var datas = data.data
            var str = '';
            for(var i=0;i<datas.length;i++){
                str +='<div class="bc_bk">'+
                    '<a href=""><span class="bc_icon glyphicon glyphicon-trash"></span></a>' +
                    '<div class="bc_img">' +
                    '<a href="details_buy.html">' +
                    '<img src="img/book_05.jpg" />' +
                    '</a>' +
                    '</div>' +
                    '<div class="bc_info">'+
                    '<ul>' +
                    '<li>名称：<span>情书</span></li>' +
                    '<li>价格：<span>26.5 元</span></li>' +
                    '<li>时间：<span>2019.12.22</span></li>' +
                    '<li>成色：<span>七成新</span></li>' +
                    '<li>库存：<span>目前还有八本</span></li>' +
                    '<li>卖家：<span>山西财经大学信息学院学生</span></li>' +
                    '</ul>'+
                    '<button id="bc_btn" class="btn btn-default" onclick="window.open(\'client.html\')">购买</button>'+
                    '</div>'+
                    '</div>';
            }
            $("#bc_info").html(str);
		},
        error:function(response){
        alert("失败！")
    }
	});
});