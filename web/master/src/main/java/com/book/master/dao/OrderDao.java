package com.book.master.dao;

import com.book.master.bean.TabBook;
import com.book.master.bean.TabOrder;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface OrderDao extends JpaRepository<TabOrder,Integer> {
    List<TabOrder> findByUid(Integer uid);
}
