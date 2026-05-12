





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String email;
    private String Branch;
    private String Department;
    private String class;
    private String name;
    private String password;



    public Account(
        String email,        String Branch,        String Department,        String class,        String name,        String password    ) {
        this.email = email;
        this.Branch = Branch;
        this.Department = Department;
        this.class = class;
        this.name = name;
        this.password = password;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getBranch() {
        return Branch;
    }

    public void setBranch(String Branch) {
        this.Branch = Branch;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public String getClass() {
        return class;
    }

    public void setClass(String class) {
        this.class = class;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}