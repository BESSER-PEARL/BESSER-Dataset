





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int EmployeeID;
    private String Role;
    private int StoreID;
    private float Salary;





    private Store store;


    public Employee(
        int EmployeeID,        String Role,        int StoreID,        float Salary    ) {
        this.EmployeeID = EmployeeID;
        this.Role = Role;
        this.StoreID = StoreID;
        this.Salary = Salary;
    }


    public int getEmployeeid() {
        return EmployeeID;
    }

    public void setEmployeeid(int EmployeeID) {
        this.EmployeeID = EmployeeID;
    }
    public String getRole() {
        return Role;
    }

    public void setRole(String Role) {
        this.Role = Role;
    }
    public int getStoreid() {
        return StoreID;
    }

    public void setStoreid(int StoreID) {
        this.StoreID = StoreID;
    }
    public float getSalary() {
        return Salary;
    }

    public void setSalary(float Salary) {
        this.Salary = Salary;
    }

    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}