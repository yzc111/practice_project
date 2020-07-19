package com.book.master.controller;

import com.book.master.bean.TabBook;
import com.book.master.bean.TabUser;
import com.book.master.service.BookService;
import com.book.master.service.UserService;
import com.book.master.util.JsonResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.List;

@RestController
@RequestMapping("/book")
public class BookController {

    @Autowired
    private BookService bookService;

    @Autowired
    private UserService userService;

    @GetMapping("/saveBook")
    public JsonResult saveBook(TabBook tabBook,TabUser user){
        try {
            TabUser byName = userService.findByName(user.getName());
            tabBook.setUid(byName.getId());
            bookService.saveBook(tabBook);
            return new JsonResult(0,"成功！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }
    @GetMapping("/findByUid")
    public JsonResult findByUid(TabUser user){
        try {
            TabUser byName = userService.findByName(user.getName());
            if(byName!=null){
                List<TabBook> books = bookService.findByUid(byName.getId());
                return new JsonResult(0,"成功！",books);
            }
            return new JsonResult(0,"成功！",null);
        } catch (Exception e) {
            e.printStackTrace();
            return new JsonResult(101,"服务异常！",null);
        }
    }

}
