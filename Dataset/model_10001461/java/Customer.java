





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String sem;
    private String password;
    private String branch;
    private String email;
    private int phone;
    private String name;



    public Customer(
        String sem,        String password,        String branch,        String email,        int phone,        String name    ) {
        this.sem = sem;
        this.password = password;
        this.branch = branch;
        this.email = email;
        this.phone = phone;
        this.name = name;
    }


    public String getSem() {
        return sem;
    }

    public void setSem(String sem) {
        this.sem = sem;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}