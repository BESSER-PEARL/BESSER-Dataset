




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class demo_model_Employee  {

    private String firstname;
    private String phone;
    private String position;
    private String lastname;
    private String email;
    private LocalDate birthday;





    private demo_model_Company demo_model_company;




    private demo_model_Company demo_model_company;


    public demo_model_Employee(
        String firstname,        String phone,        String position,        String lastname,        String email,        LocalDate birthday    ) {
        this.firstname = firstname;
        this.phone = phone;
        this.position = position;
        this.lastname = lastname;
        this.email = email;
        this.birthday = birthday;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public LocalDate getBirthday() {
        return birthday;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }

    public demo_model_Company getDemo_model_company() {
        return demo_model_company;
    }

    public void setDemo_model_company(demo_model_Company demo_model_company) {
        this.demo_model_company = demo_model_company;
    }
    public demo_model_Company getDemo_model_company() {
        return demo_model_company;
    }

    public void setDemo_model_company(demo_model_Company demo_model_company) {
        this.demo_model_company = demo_model_company;
    }

}