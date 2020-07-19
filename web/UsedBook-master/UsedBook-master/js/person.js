//个人中心模块的根目录栏
$(document).ready(function () {
	// var name = JSON.parse(localStorage.getItem("name"))
	$.ajax({
		url:'http://127.0.0.1:9090/user/getUserInfo',
		type:'get',
        contentType: "application/json;charset=utf-8",
		dataType:'json',
		data:{name:localStorage.getItem("name")},
		success:function(data){
            document.getElementById('name').value=data.data.name;
            document.getElementById('gender').value=data.data.gender;
            document.getElementById('age').value=data.data.age;
            document.getElementById('email').value=data.data.email;
            document.getElementById('place').value=data.data.place;
            document.getElementById('introduce').value=data.data.introduce;
		},
		error:function(response){
			alert("失败！")
		}
	});
});
$(function(){
	var $div = $("#per_person");
	$(window).scroll(function(){
		var height = $div.offset().top - $(window).scrollTop();
		if(height <= 60 ){
			$div.addClass("window_move").removeClass("window_on");
		}
		var height_2 = $div.offset().top;
		if(height_2 < 245){
			$div.addClass("window_on").removeClass("window_move");
		}
	})
})

//更换头像

$(function(){
	$("#per_btn_h3").click(function(){
		$(".per_second").hide();
	})
	$("#per_btn_img").click(function(){
		$(".per_second").show();
	})
	
})


//个人中心模块的信息
//<button id="per_fir_btn" class="btn btn-default">提交</button>
//<button id="per_pas_btn" class="btn btn-default">确定修改</button>
$(function(){
	$("#per_btn ").click(function(){
		$(".per_first").toggle();
		$(".per_first_2").toggle();
	});
	$("#per_pas_btn").click(function(){
		$(".per_first").toggle();
		$(".per_first_2").toggle();
		alert("密码修改成功！感谢你的支持！");
	});
	$("#per_fir_btn").click(function(){
		alert("用户信息提交成功！感谢你的支持！")
	});
})