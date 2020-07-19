package com.book.master.bean;

import lombok.Data;
import lombok.Generated;

import javax.persistence.*;

@Table(name = "user")
@Data
@Entity
public class TabUser {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Integer id;
    private String name;
    private Integer gender;
    private Integer age;
    private String email;
    private String place;
    private String introduce;
    private String password;
}
