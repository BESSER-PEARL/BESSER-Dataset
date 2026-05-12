





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private int Emp_Id;
    private float Sly_Increment;
    private float Sly_Decrement;
    private float Sly_Netgross;
    private String OverTime;
    private float Sly_Basic;





    private Employee employee;


    public Salary(
        int Emp_Id,        float Sly_Increment,        float Sly_Decrement,        float Sly_Netgross,        String OverTime,        float Sly_Basic    ) {
        this.Emp_Id = Emp_Id;
        this.Sly_Increment = Sly_Increment;
        this.Sly_Decrement = Sly_Decrement;
        this.Sly_Netgross = Sly_Netgross;
        this.OverTime = OverTime;
        this.Sly_Basic = Sly_Basic;
    }


    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public float getSly_increment() {
        return Sly_Increment;
    }

    public void setSly_increment(float Sly_Increment) {
        this.Sly_Increment = Sly_Increment;
    }
    public float getSly_decrement() {
        return Sly_Decrement;
    }

    public void setSly_decrement(float Sly_Decrement) {
        this.Sly_Decrement = Sly_Decrement;
    }
    public float getSly_netgross() {
        return Sly_Netgross;
    }

    public void setSly_netgross(float Sly_Netgross) {
        this.Sly_Netgross = Sly_Netgross;
    }
    public String getOvertime() {
        return OverTime;
    }

    public void setOvertime(String OverTime) {
        this.OverTime = OverTime;
    }
    public float getSly_basic() {
        return Sly_Basic;
    }

    public void setSly_basic(float Sly_Basic) {
        this.Sly_Basic = Sly_Basic;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}