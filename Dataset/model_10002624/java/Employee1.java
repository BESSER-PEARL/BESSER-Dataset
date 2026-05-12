





import java.util.List;
import java.util.ArrayList;

public class Employee1  {

    private int contact_no;
    private String UserName;
    private int Salary;
    private String name;
    private String Emp_Address;
    private String attribute;
    private String password;
    private String Emp_Dep;
    private String Email;





    private Admin1 admin1;


    public Employee1(
        int contact_no,        String UserName,        int Salary,        String name,        String Emp_Address,        String attribute,        String password,        String Emp_Dep,        String Email    ) {
        this.contact_no = contact_no;
        this.UserName = UserName;
        this.Salary = Salary;
        this.name = name;
        this.Emp_Address = Emp_Address;
        this.attribute = attribute;
        this.password = password;
        this.Emp_Dep = Emp_Dep;
        this.Email = Email;
    }


    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getSalary() {
        return Salary;
    }

    public void setSalary(int Salary) {
        this.Salary = Salary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmp_address() {
        return Emp_Address;
    }

    public void setEmp_address(String Emp_Address) {
        this.Emp_Address = Emp_Address;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmp_dep() {
        return Emp_Dep;
    }

    public void setEmp_dep(String Emp_Dep) {
        this.Emp_Dep = Emp_Dep;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public Admin1 getAdmin1() {
        return admin1;
    }

    public void setAdmin1(Admin1 admin1) {
        this.admin1 = admin1;
    }

}