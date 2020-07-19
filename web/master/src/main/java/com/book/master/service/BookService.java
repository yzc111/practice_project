package com.book.master.service;

import com.book.master.bean.TabBook;
import com.book.master.dao.BookDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    private BookDao bookDao;

    public void saveBook(TabBook tabBook){
        bookDao.save(tabBook);
    }
    public List<TabBook> findByUid(Integer uid){
       return bookDao.findByUid(uid);
    }

}
