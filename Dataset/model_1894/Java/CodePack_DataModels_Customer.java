




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_Customer  {

    private String last_name;
    private String first_name;
    private int payment_id;
    private LocalDate date_of_birth;
    private String e_mail;
    private int bonus_points;
    private int phone_no;
    private int customer_id;
    private String password;



    public CodePack_DataModels_Customer(
        String last_name,        String first_name,        int payment_id,        LocalDate date_of_birth,        String e_mail,        int bonus_points,        int phone_no,        int customer_id,        String password    ) {
        this.last_name = last_name;
        this.first_name = first_name;
        this.payment_id = payment_id;
        this.date_of_birth = date_of_birth;
        this.e_mail = e_mail;
        this.bonus_points = bonus_points;
        this.phone_no = phone_no;
        this.customer_id = customer_id;
        this.password = password;
    }


    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public int getPayment_id() {
        return payment_id;
    }

    public void setPayment_id(int payment_id) {
        this.payment_id = payment_id;
    }
    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public String getE_mail() {
        return e_mail;
    }

    public void setE_mail(String e_mail) {
        this.e_mail = e_mail;
    }
    public int getBonus_points() {
        return bonus_points;
    }

    public void setBonus_points(int bonus_points) {
        this.bonus_points = bonus_points;
    }
    public int getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(int phone_no) {
        this.phone_no = phone_no;
    }
    public int getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}