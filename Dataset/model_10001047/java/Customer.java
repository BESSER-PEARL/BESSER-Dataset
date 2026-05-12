





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private String sem;
    private String branch;
    private int phone;
    private String email;
    private String password;



    public Customer(
        String name,        String sem,        String branch,        int phone,        String email,        String password    ) {
        this.name = name;
        this.sem = sem;
        this.branch = branch;
        this.phone = phone;
        this.email = email;
        this.password = password;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}