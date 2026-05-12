





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String UserName;
    private String Password;
    private String UserType;





    private Employee employee;


    public Admin(
        String UserName,        String Password,        String UserType    ) {
        this.UserName = UserName;
        this.Password = Password;
        this.UserType = UserType;
    }


    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsertype() {
        return UserType;
    }

    public void setUsertype(String UserType) {
        this.UserType = UserType;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}