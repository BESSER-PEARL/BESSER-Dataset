




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class demo_model_Employee  {

    private String lastname;
    private LocalDate birthday;
    private String phone;
    private String email;
    private String position;
    private String firstname;





    private demo_model_Company demo_model_company;




    private demo_model_Company demo_model_company;




    private demo_model_Address demo_model_address;


    public demo_model_Employee(
        String lastname,        LocalDate birthday,        String phone,        String email,        String position,        String firstname    ) {
        this.lastname = lastname;
        this.birthday = birthday;
        this.phone = phone;
        this.email = email;
        this.position = position;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public LocalDate getBirthday() {
        return birthday;
    }

    public void setBirthday(LocalDate birthday) {
        this.birthday = birthday;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
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
    public demo_model_Address getDemo_model_address() {
        return demo_model_address;
    }

    public void setDemo_model_address(demo_model_Address demo_model_address) {
        this.demo_model_address = demo_model_address;
    }

}