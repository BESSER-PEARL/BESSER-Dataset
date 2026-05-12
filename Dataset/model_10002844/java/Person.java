





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private int phone;
    private String email;
    private String name;



    public Person(
        int phone,        String email,        String name    ) {
        this.phone = phone;
        this.email = email;
        this.name = name;
    }


    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}