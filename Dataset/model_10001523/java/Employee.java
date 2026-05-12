





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String EmplyeeName;
    private String EmployeeId;
    private String EmployeeEmail;
    private int EmployeePhoneNumber;





    private Login login;


    public Employee(
        String EmplyeeName,        String EmployeeId,        String EmployeeEmail,        int EmployeePhoneNumber    ) {
        this.EmplyeeName = EmplyeeName;
        this.EmployeeId = EmployeeId;
        this.EmployeeEmail = EmployeeEmail;
        this.EmployeePhoneNumber = EmployeePhoneNumber;
    }


    public String getEmplyeename() {
        return EmplyeeName;
    }

    public void setEmplyeename(String EmplyeeName) {
        this.EmplyeeName = EmplyeeName;
    }
    public String getEmployeeid() {
        return EmployeeId;
    }

    public void setEmployeeid(String EmployeeId) {
        this.EmployeeId = EmployeeId;
    }
    public String getEmployeeemail() {
        return EmployeeEmail;
    }

    public void setEmployeeemail(String EmployeeEmail) {
        this.EmployeeEmail = EmployeeEmail;
    }
    public int getEmployeephonenumber() {
        return EmployeePhoneNumber;
    }

    public void setEmployeephonenumber(int EmployeePhoneNumber) {
        this.EmployeePhoneNumber = EmployeePhoneNumber;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}