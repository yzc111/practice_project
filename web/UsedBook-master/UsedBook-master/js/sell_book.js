
//个人中心页面部分的验证
$(function(){
	$(function(){
        //文本框失去焦点后
        $('form :input').blur(function(){
            var $parent = $(this).parent();
            $parent.find(".formtips").remove();
            //验证书籍名
            if( $(this).is('#book_name') ){
                if( this.value=="" ){
                    var ErrorMsg = '书名不能为空';
                    $parent.append('<span class="formtips bookError">'+ErrorMsg+'</span>');
                }
            }
            //书籍主标题
            if($(this).is('#info')){
                if( this.value=="" || this.value.length > 20){
                    var ErrorM = '请把字数控制在20字以内，不能为空';
                    $parent.append('<span class="formtips bookError">' + ErrorM +'</span>');
                }
            }
            //书籍副标题
            if($(this).is('#info_2')){
                if( this.value=="" || this.value > 50 ){
                    var ErrorMa = '50字以内就行';
                    $parent.append('<span class="formtips bookError">' + ErrorMa +'</span>');
                }
            }
            //验证是否选择照片
            if($(this).is('#fild_text')){
                if( this.value=="" ){
                    var ErrorMa = '请选择照片';
                    $parent.append('<span class="formtips bookError">' + ErrorMa +'</span>');
                }
            }
            //验证是否报价
            if($(this).is('#book_cash')){
                if( this.value=="" ){
                    var ErrorMa = '请合理报价';
                    $parent.append('<span class="formtips bookError">' + ErrorMa +'</span>');
                }
            }
            //验证附加是否为空
            if($(this).is('#info_addr')){
                if( this.value==""){
                    var ErrorMa = '总的说点什么吧';
                    $parent.append('<span class="formtips bookError">' + ErrorMa +'</span>');
                }
            }
        }).keyup(function(){
            $(this).triggerHandler("blur");
        }).focus(function(){
            $(this).triggerHandler("blur");
        });//end blur


        //提交，最终验证。
        $('#sk_btn').click(function(){
        	$("form :input.required").trigger('blur');
            var bookError = $('form .bookError').length;
            if(bookError){
            	alert("请完善你的个人资料，不然无法提交");
                return false;
            }
            else{
                alert("你的书籍提交成功");
                window.open ("home_page.html","_blank");
            }
        });

    })
})