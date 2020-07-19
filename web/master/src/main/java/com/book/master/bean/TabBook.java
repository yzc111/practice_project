package com.book.master.bean;
import lombok.Data;
import javax.persistence.*;
@Table(name = "book")
@Data
@Entity
public class TabBook {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Integer id;
    private String nam;
    private String intro;
    private String price;
    private String lag;
    private String typ;
    private String cond;
    private String ctime;
    private String stock;
    private String seller;
    private Integer uid;
}
