





import java.util.List;
import java.util.ArrayList;

public class employee  {

    private String password;
    private String department;



    public employee(
        String password,        String department    ) {
        this.password = password;
        this.department = department;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }


}