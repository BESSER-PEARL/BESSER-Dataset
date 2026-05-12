





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Password;
    private String User_Name;





    private List<Employee> employees;


    public Login(
        String Password,        String User_Name    ) {
        this.Password = Password;
        this.User_Name = User_Name;
        this.employees = new ArrayList<>();
    }

    public Login(
        String Password,        String User_Name        ArrayList<Employee> employees    ) {
        this.Password = Password;
        this.User_Name = User_Name;
        this.employees = employees;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUser_name() {
        return User_Name;
    }

    public void setUser_name(String User_Name) {
        this.User_Name = User_Name;
    }

    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}