





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String OverTime;
    private float Sly_Decrement;
    private int Emp_Id;
    private float Sly_Netgross;
    private float Sly_Basic;
    private float Sly_Increment;





    private Manager manager;


    public Salary(
        String OverTime,        float Sly_Decrement,        int Emp_Id,        float Sly_Netgross,        float Sly_Basic,        float Sly_Increment    ) {
        this.OverTime = OverTime;
        this.Sly_Decrement = Sly_Decrement;
        this.Emp_Id = Emp_Id;
        this.Sly_Netgross = Sly_Netgross;
        this.Sly_Basic = Sly_Basic;
        this.Sly_Increment = Sly_Increment;
    }


    public String getOvertime() {
        return OverTime;
    }

    public void setOvertime(String OverTime) {
        this.OverTime = OverTime;
    }
    public float getSly_decrement() {
        return Sly_Decrement;
    }

    public void setSly_decrement(float Sly_Decrement) {
        this.Sly_Decrement = Sly_Decrement;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public float getSly_netgross() {
        return Sly_Netgross;
    }

    public void setSly_netgross(float Sly_Netgross) {
        this.Sly_Netgross = Sly_Netgross;
    }
    public float getSly_basic() {
        return Sly_Basic;
    }

    public void setSly_basic(float Sly_Basic) {
        this.Sly_Basic = Sly_Basic;
    }
    public float getSly_increment() {
        return Sly_Increment;
    }

    public void setSly_increment(float Sly_Increment) {
        this.Sly_Increment = Sly_Increment;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}