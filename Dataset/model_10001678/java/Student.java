





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String surname;
    private String email;
    private String phone;
    private String name;



    public Student(
        String surname,        String email,        String phone,        String name    ) {
        this.surname = surname;
        this.email = email;
        this.phone = phone;
        this.name = name;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}