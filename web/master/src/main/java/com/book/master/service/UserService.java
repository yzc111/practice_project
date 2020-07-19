package com.book.master.service;

import com.book.master.bean.TabUser;
import com.book.master.dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UserDao userDao;

    public void saveUser(TabUser user){
        userDao.save(user);
    }

    public TabUser login(String name,String pass){
       return userDao.findByNameAndPassword(name,pass);
    }
    public TabUser findByName(String name){
       return userDao.findByName(name);
    }
}
