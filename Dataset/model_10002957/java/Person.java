




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String last_name;
    private LocalDate date_of_birth;
    private String first_name;
    private String address;
    private String telephone;
    private None sex;



    public Person(
        String last_name,        LocalDate date_of_birth,        String first_name,        String address,        String telephone,        None sex    ) {
        this.last_name = last_name;
        this.date_of_birth = date_of_birth;
        this.first_name = first_name;
        this.address = address;
        this.telephone = telephone;
        this.sex = sex;
    }


    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public None getSex() {
        return sex;
    }

    public void setSex(None sex) {
        this.sex = sex;
    }


}