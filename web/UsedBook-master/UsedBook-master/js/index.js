//书库部分关于书籍图片的处理
$(function(){
	$(".right_books").hover(function(){
		$(this).addClass("find_fa").css("border-bottom","2px solid #48B30F")
			.siblings().removeClass("find_fa").css("border-bottom","2px solid #FFFFFF");
		$(".find_fa").find(".hidden_span").fadeIn();
	}).mouseleave(function(){
		$(".find_fa").css("border-bottom","2px solid #FFFFFF").find(".hidden_span").fadeOut();
	});
	$(".left_books").hover(function(){
		$(this).addClass("find_fa_left").css("border-bottom","2px solid #48B30F")
			.siblings().removeClass("find_fa_left").css("border-bottom","2px solid #FFFFFF");
		$(".find_fa_left").find(".hidden_span_left").fadeIn();
	}).mouseleave(function(){
		$(".find_fa_left").css("border-bottom","2px solid #FFFFFF").find(".hidden_span_left").fadeOut();
	})
})

//书库部分按钮的文字改变
$(function(){
	$(".btn_find").hover(function(){
		$(this).children().html("GO");
	}).mouseout(function(){
		$(this).children().html("去看看");
	})
})

//书库部分按钮背景颜色的改变
$(function(){
	$('.screen li').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
	})
})

//心愿单部分的按钮内容改变
$(function(){
	$(".list_btn").hover(function(){
		$(this).children().html("我去写");
	}).mouseout(function(){
		$(this).children().html("我也想");
	})
})

//首页部分切换公告栏和活动栏
$(function(){
	$('.sec_ul_1').show();
	$(".index_li_1").hover(function(){
		$(".sec_ul_2").hide();
		$(".sec_ul_1").show();
	})
	$(".index_li_2").hover(function(){
		$(".sec_ul_2").show();
		$(".sec_ul_1").hide();
	})
})

//书籍详情页面的图片的显示
$(function(){
	var $li_1=$('.book_ul_1 img');
	var $li_2=$('.book_ul_2 li');
	var index=0;
	$li_2.hover(function(){
		index=$(this).index();
		$li_1.eq(index).addClass("img_find").show()
			.siblings().removeClass("img_find").hide();
	})
})

//心愿单详情页面的点赞动画
$(function(){
	$(".ld_icon").click(function(){
		$(this).css("color","red");
	})
})

//书架部分的图标显示
$(function(){
	$("#bc_book_btn").click(function(){
		$(".bc_icon").toggle();
	})
	$("#bc_wish_btn").click(function(){
		$(".bc_list_icon").toggle();
	})
	$(".bc_icon").click(function(){
		$(this).parent().remove();
	})
	$(".bc_list_icon").click(function(){
		$(this).parent().remove();
	})
})


//个人中心部分的隐藏与显示
$(function(){
	$("#per_btn ").click(function(){
		$(".per_first").toggle();
		$(".per_first_2").toggle();
	})
})

//论坛的评论隐藏和显示
$(function(){
	$(".com_icon_btn").click(function(){
		$(".com_hide").show();
		$(this).hide();
		$(".com_icon_btn_2").show();
	})
	$(".com_icon_btn_2").click(function(){
		$(".com_hide").hide();
		$(this).hide();
		$(".com_icon_btn").show();
	})
})

//物品详情页面的交易按钮
$(function(){
	$("#details_link").click(function(){
		$(".details_fix").show();
	})
	$("#details_fix_btn").click(function(){
		$(".details_fix").hide();
	})
})

//心愿单详情页面的交易按钮
$(function(){
	$("#ld_btn").click(function(){
		$(".ld_fix").show();
	})
	$("#ld_fix_btn").click(function(){
		$(".ld_fix").hide();
	})
})

////书库页面的下一页按钮
//$(function(){
//	$("#stack_ul_btn").click(function(){
//		var li_index=$("#ul_icon>li").eq().hasClass("active");
//		alert(li_index);
//	})
//})
//书库页面的下面的分页
$(function(){
	$("#ul_icon>li").click(function(){
		$(this).addClass("active")
			.siblings().removeClass("active");
	})
})


$(function(){
	$(function(){
        //文本框失去焦点后
        $('form :input').blur(function(){
            var $parent = $(this).parent();
            $parent.find(".formtips").remove();
            //验证用户名
            if( $(this).is('#name') ){
                if( this.value=="" || this.value.length < 4 || this.value.length > 8 ){
                    var ErrorMsg = '用户名长度在4到8位之间';
                    $parent.append('<span class="formtips onError">'+ErrorMsg+'</span>');
                }else{
                    var OkMsg = '输入正确.';
                    $parent.append('<span class="formtips onSuccess">'+OkMsg+'</span>');
                }
            }
            //验证密码
            if($(this).is('#password')){
                if( this.value=="" || this.value.length < 6 ){
                    var ErrorM = '请输入至少6位的密码。';
                    $parent.append('<span class="formtips onError">' + ErrorM +'</span>');
                }
                else{
                    var OkM ='输入正确.';
                    $parent.append('<span class="formtips onSuccess">' + OkM + '</span>')
                }
            }
            //再次验证密码
            if($(this).is('#repassword')){
                if( this.value=="" || this.value!=password.value ){
                    var ErrorMa = '与上面的密码不一致';
                    $parent.append('<span class="formtips onError">' + ErrorMa +'</span>');
                }
                else{
                    var OkMa ='输入正确.';
                    $parent.append('<span class="formtips onSuccess">' + OkMa + '</span>')
                }
            }
            //验证邮件
            if( $(this).is('#email') ){
                if( this.value=="" || ( this.value!="" && !/.+@.+\.[a-zA-Z]{2,4}$/.test(this.value) ) ){
                    var EorMsg = '请输入正确的E-Mail地址.';
                    $parent.append('<span class="formtips onError">'+EorMsg+'</span>');
                }else{
                    var kMsg = '输入正确.';
                    $parent.append('<span class="formtips onSuccess">'+kMsg+'</span>');
                }
            }

            //验证验证是否为空
            // if($(this).is('#ver_code')){
            // 	if( this.value==""){
            // 		var code_mes = '验证码必须填写';
            // 		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            // 	}
            // }
            if($(this).is('#gender')){
            	if( this.value==""){
            		var code_mes = '性别必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            } if($(this).is('#age')){
            	if( this.value==""){
            		var code_mes = '年龄必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            }if($(this).is('#place')){
            	if( this.value==""){
            		var code_mes = '住址必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            }if($(this).is('#introduce')){
            	if( this.value==""){
            		var code_mes = '自我介绍必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            }if($(this).is('#name')){
            	if( this.value==""){
            		var code_mes = '用户名必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            }if($(this).is('#password')){
            	if( this.value==""){
            		var code_mes = '密码必须填写';
            		$parent.append('<span class="formtips onError">'+code_mes+'</span>');
            	}
            }
            //$("input[type='checkbox']").is(':checked')
            //验证checkbox是否确认
            if($(this).is('#address')){
            	if(this.ckecked){
            		var addr_mes = '谢谢你的支持';
            		$parent.append('<span class="formtips onError">'+addr_mes+'</span>');
            	}else{
            		var addr_mes = '只有同意协议才能注册';
            		$parent.append('<span class="formtips onError">'+addr_mes+'</span>');
            	}
            }
            
        }).keyup(function(){
            $(this).triggerHandler("blur");
        }).focus(function(){
            $(this).triggerHandler("blur");
        });//end blur


        //提交，最终验证。
        $('#login_btn').click(function(){
            $("form :input.required").trigger('blur');
            var numError = $('form .onError').length;
            if(numError){

                return false;
            }
            else{
                $.ajax({
                    url:'http://127.0.0.1:9090/user/saveUser',
                    type:'get',
                    dataType:'json',
                    contentType: "application/json;charset=utf-8",
                    data:{name:$('#name').val(),password:$('#password').val(),gender:$('#gender').val(),age:$('#age').val(),email:$('#email').val(),place:$('#place').val(),introduce:$('#introduce').val()},
                    success:function(data){
                        if(data.state===0){
                            alert("注册成功，请登录！")
                            window.location.href="login.html";
                        }else{
                            alert("登陆失败!")
                        }
                        //请求成功后执行的代码
                    },
                    error:function(data){
                        alert("失败！")
                        //失败后执行的代码
                    }
                });
            }
        });

        //重置
        $('#res').click(function(){
            $(".formtips").remove();
        });
    })
})
//
$(function(){
	$('#sub').click(function(){
		$.ajax({
			url:'http://localhost:9090/user/login',
			type:'get',
			dataType:'json',
            contentType: "application/json;charset=utf-8",
			data:{name:$('#name').val(),pass:$('#pass').val()},
			success:function(data){
				if(data.state===0){
					alert("登陆成功!")
                    window.location.href="home_page.html";
                    localStorage.setItem("name",$('#name').val())
				}else{
					alert("登陆失败!")
				}
				//请求成功后执行的代码
			},
			error:function(data){
				alert("登录失败！")
				//失败后执行的代码
			}
		});
	})
})
var i=0;
    $('#subOrder').click(function(){
        $.ajax({
        	url:'http://127.0.0.1:9090/order/saveOrder',
        	type:'get',
        	dataType:'json',
        	data:{name:localStorage.getItem("name"),addre:$('#addre').val(),people:$('#people').val(),phone:$('#phone').val(),prodname:"计算机网络技术",unitprice:26.5,cou:1,totalprice:26.5},
        	success:function(data){
                if(i===0){
                    i++
                    alert("成功！")
				}
                window.location.href="order.html";
        		//请求成功后执行的代码
        	},
        	error:function(data){
                if(i===0){
                    alert("失败！")
                }
        		//失败后执行的代码
        	}
        });
    })