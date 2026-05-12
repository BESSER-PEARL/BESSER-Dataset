





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String password;
    private String name;
    private int phone;
    private String email;
    private String sem;
    private String branch;



    public Customer(
        String password,        String name,        int phone,        String email,        String sem,        String branch    ) {
        this.password = password;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.sem = sem;
        this.branch = branch;
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
    public String getSem() {
        return sem;
    }

    public void setSem(String sem) {
        this.sem = sem;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }


}