package com.book.master.service;

import com.book.master.bean.TabBook;
import com.book.master.bean.TabOrder;
import com.book.master.dao.BookDao;
import com.book.master.dao.OrderDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class OrderService {
    @Autowired
    private OrderDao orderDao;

    public void saveOrder(TabOrder order){
        orderDao.save(order);
    }
    public List<TabOrder> findOrder(Integer uid){
        return orderDao.findByUid(uid);
    }

}
