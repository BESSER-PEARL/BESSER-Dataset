





import java.util.List;
import java.util.ArrayList;

public class Account_for_employee  {

    private String getaccount;
    private String attribute;
    private String name;
    private String email;
    private String id;
    private String password;



    public Account_for_employee(
        String getaccount,        String attribute,        String name,        String email,        String id,        String password    ) {
        this.getaccount = getaccount;
        this.attribute = attribute;
        this.name = name;
        this.email = email;
        this.id = id;
        this.password = password;
    }


    public String getGetaccount() {
        return getaccount;
    }

    public void setGetaccount(String getaccount) {
        this.getaccount = getaccount;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}