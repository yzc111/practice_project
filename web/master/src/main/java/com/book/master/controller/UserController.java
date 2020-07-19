package com.book.master.controller;

import com.book.master.bean.TabUser;
import com.book.master.service.UserService;
import com.book.master.util.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/login")
    public JsonResult login(String name, String pass,HttpServletRequest request){
        try {
            TabUser login = userService.login(name, pass);
            HttpSession session = request.getSession();
            session.setAttribute("uid",login.getId());
            if(login!=null){
                return new JsonResult(0,"登录成功！",null);
            }
            return new JsonResult(102,"登陆失败！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }
    @GetMapping("/saveUser")
    public JsonResult saveUser(TabUser user){
        try {
            userService.saveUser(user);
            return new JsonResult(0,"成功！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }

    @GetMapping("/getUserInfo")
    public JsonResult getUserInfo(TabUser user){
        try {
            TabUser login = userService.findByName(user.getName());
            if(login!=null){
                return new JsonResult(0,"成功！",login);
            }
            return new JsonResult(102,"失败！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }

}
