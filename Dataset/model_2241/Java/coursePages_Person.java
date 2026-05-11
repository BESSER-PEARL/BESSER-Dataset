





import java.util.List;
import java.util.ArrayList;

public class coursePages_Person  {

    private String firstName;
    private String surName;
    private String phoneNummber;
    private String email;



    public coursePages_Person(
        String firstName,        String surName,        String phoneNummber,        String email    ) {
        this.firstName = firstName;
        this.surName = surName;
        this.phoneNummber = phoneNummber;
        this.email = email;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getSurname() {
        return surName;
    }

    public void setSurname(String surName) {
        this.surName = surName;
    }
    public String getPhonenummber() {
        return phoneNummber;
    }

    public void setPhonenummber(String phoneNummber) {
        this.phoneNummber = phoneNummber;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}