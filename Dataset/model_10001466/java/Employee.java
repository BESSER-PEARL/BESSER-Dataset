





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String EmpName;
    private String EmpPassword;
    private String EmployeeID;





    private Orders orders;


    public Employee(
        String EmpName,        String EmpPassword,        String EmployeeID    ) {
        this.EmpName = EmpName;
        this.EmpPassword = EmpPassword;
        this.EmployeeID = EmployeeID;
    }


    public String getEmpname() {
        return EmpName;
    }

    public void setEmpname(String EmpName) {
        this.EmpName = EmpName;
    }
    public String getEmppassword() {
        return EmpPassword;
    }

    public void setEmppassword(String EmpPassword) {
        this.EmpPassword = EmpPassword;
    }
    public String getEmployeeid() {
        return EmployeeID;
    }

    public void setEmployeeid(String EmployeeID) {
        this.EmployeeID = EmployeeID;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}