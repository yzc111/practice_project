package com.book.master.controller;

import com.book.master.bean.TabBook;
import com.book.master.bean.TabOrder;
import com.book.master.bean.TabUser;
import com.book.master.service.BookService;
import com.book.master.service.OrderService;
import com.book.master.service.UserService;
import com.book.master.util.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpSession;
import java.util.List;

@RestController
@RequestMapping("/order")
public class OrderController {

    @Autowired
    private OrderService orderService;

    @Autowired
    private UserService userService;


    @GetMapping("/saveOrder")
    public JsonResult saveOrder(TabOrder order, TabUser user){
        try {
            TabUser byName = userService.findByName(user.getName());
            order.setUid(byName.getId());
            orderService.saveOrder(order);
            return new JsonResult(0,"成功！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }
    @GetMapping("/findOrder")
    public JsonResult findOrder(TabUser user){
        try {
            TabUser byName = userService.findByName(user.getName());
            List<TabOrder> order = orderService.findOrder(byName.getId());
            return new JsonResult(0,"成功！",order);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }

}
