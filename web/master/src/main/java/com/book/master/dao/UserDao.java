package com.book.master.dao;

import com.book.master.bean.TabUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserDao extends JpaRepository<TabUser,Integer> {

    TabUser findByNameAndPassword(String name,String pass);
    TabUser findByName(String name);

}
