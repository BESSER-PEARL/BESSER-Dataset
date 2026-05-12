





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private String Sly_Basic;
    private String Emp_Id;
    private String Sly_Netgross;
    private None Sly_Increment;
    private String Sly_Decrement;
    private String OverTime;





    private User user;


    public Salary(
        String Sly_Basic,        String Emp_Id,        String Sly_Netgross,        None Sly_Increment,        String Sly_Decrement,        String OverTime    ) {
        this.Sly_Basic = Sly_Basic;
        this.Emp_Id = Emp_Id;
        this.Sly_Netgross = Sly_Netgross;
        this.Sly_Increment = Sly_Increment;
        this.Sly_Decrement = Sly_Decrement;
        this.OverTime = OverTime;
    }


    public String getSly_basic() {
        return Sly_Basic;
    }

    public void setSly_basic(String Sly_Basic) {
        this.Sly_Basic = Sly_Basic;
    }
    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getSly_netgross() {
        return Sly_Netgross;
    }

    public void setSly_netgross(String Sly_Netgross) {
        this.Sly_Netgross = Sly_Netgross;
    }
    public None getSly_increment() {
        return Sly_Increment;
    }

    public void setSly_increment(None Sly_Increment) {
        this.Sly_Increment = Sly_Increment;
    }
    public String getSly_decrement() {
        return Sly_Decrement;
    }

    public void setSly_decrement(String Sly_Decrement) {
        this.Sly_Decrement = Sly_Decrement;
    }
    public String getOvertime() {
        return OverTime;
    }

    public void setOvertime(String OverTime) {
        this.OverTime = OverTime;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}