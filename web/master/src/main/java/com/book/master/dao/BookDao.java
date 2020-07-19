package com.book.master.dao;

import com.book.master.bean.TabBook;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BookDao extends JpaRepository<TabBook,Integer> {
    List<TabBook> findByUid(Integer uid);
}
