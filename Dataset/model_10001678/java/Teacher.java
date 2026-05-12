





import java.util.List;
import java.util.ArrayList;

public class Teacher  {

    private String name;
    private String email;
    private String phone;
    private String surname;



    public Teacher(
        String name,        String email,        String phone,        String surname    ) {
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.surname = surname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}