





import java.util.List;
import java.util.ArrayList;

public class Driver  {

    private String password;
    private String name;
    private String id;
    private String phone;



    public Driver(
        String password,        String name,        String id,        String phone    ) {
        this.password = password;
        this.name = name;
        this.id = id;
        this.phone = phone;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}