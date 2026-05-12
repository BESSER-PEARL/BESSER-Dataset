





import java.util.List;
import java.util.ArrayList;

public class Salary  {

    private None Sly_Increment;
    private String Sly_Netgross;
    private String Emp_Id;
    private String OverTime;
    private String Sly_Basic;
    private String Sly_Decrement;





    private User user;


    public Salary(
        None Sly_Increment,        String Sly_Netgross,        String Emp_Id,        String OverTime,        String Sly_Basic,        String Sly_Decrement    ) {
        this.Sly_Increment = Sly_Increment;
        this.Sly_Netgross = Sly_Netgross;
        this.Emp_Id = Emp_Id;
        this.OverTime = OverTime;
        this.Sly_Basic = Sly_Basic;
        this.Sly_Decrement = Sly_Decrement;
    }


    public None getSly_increment() {
        return Sly_Increment;
    }

    public void setSly_increment(None Sly_Increment) {
        this.Sly_Increment = Sly_Increment;
    }
    public String getSly_netgross() {
        return Sly_Netgross;
    }

    public void setSly_netgross(String Sly_Netgross) {
        this.Sly_Netgross = Sly_Netgross;
    }
    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getOvertime() {
        return OverTime;
    }

    public void setOvertime(String OverTime) {
        this.OverTime = OverTime;
    }
    public String getSly_basic() {
        return Sly_Basic;
    }

    public void setSly_basic(String Sly_Basic) {
        this.Sly_Basic = Sly_Basic;
    }
    public String getSly_decrement() {
        return Sly_Decrement;
    }

    public void setSly_decrement(String Sly_Decrement) {
        this.Sly_Decrement = Sly_Decrement;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}