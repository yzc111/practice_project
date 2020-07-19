package com.book.master.bean;

import lombok.Data;

import javax.persistence.*;

@Table(name = "bookorder")
@Data
@Entity
public class TabOrder {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Integer id;
    private String addre;
    private String people;
    private String phone;
    private String prodname;
    private Float unitprice;
    private Integer cou;
    private Float totalprice;
    private Integer uid;
}
