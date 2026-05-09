





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Employee extends Person {

    private int employeeID;
    private int workRate;
    private float salary;



    public HotelManagementClassDiagram_Employee(
        int employeeID,        int workRate,        float salary    ) {
        super(
        );
        this.employeeID = employeeID;
        this.workRate = workRate;
        this.salary = salary;
    }


    public int getEmployeeid() {
        return employeeID;
    }

    public void setEmployeeid(int employeeID) {
        this.employeeID = employeeID;
    }
    public int getWorkrate() {
        return workRate;
    }

    public void setWorkrate(int workRate) {
        this.workRate = workRate;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }


}