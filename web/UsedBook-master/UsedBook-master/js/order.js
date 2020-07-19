$(document).ready(function () {
	$.ajax({
		url:'http://127.0.0.1:9090/order/findOrder',
		type:'get',
        contentType: "application/json;charset=utf-8",
		dataType:'json',
		data:{name:localStorage.getItem("name")},
		success:function(data){
			var datas = data.data
            var str = '<table border="1">' +
                '    <thead>' +
                '    <tr>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">配送地址</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">收件人</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">手机号</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">商品名称</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">单价</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">数量</th>' +
                '        <th style="width: 150px;text-align:center;font-size:16px">总价</th>' +
                '    </tr>' +
                '    </thead>' +
                '    <tbody>';
			for(var i=0;i<datas.length;i++){
				str += '<tr>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].addre + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].people + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].phone + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].prodname + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].unitprice + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].cou + '</td>' +
					'<td  style="width: 150px;text-align:center;font-size:14px">' + datas[i].totalprice + '</td>' +
					'</tr>';
			}
            str += '    </tbody>' +
                '</table>';
            $("#detail").html(str);
		},
		error:function(response){
			alert("失败！")
		}
	});
});