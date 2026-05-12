





import java.util.List;
import java.util.ArrayList;

public class chef  {

    private String Name;
    private int Staffid;



    public chef(
        String Name,        int Staffid    ) {
        this.Name = Name;
        this.Staffid = Staffid;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getStaffid() {
        return Staffid;
    }

    public void setStaffid(int Staffid) {
        this.Staffid = Staffid;
    }


}