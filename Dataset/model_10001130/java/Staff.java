





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String staffId;
    private String type;
    private String name;



    public Staff(
        String staffId,        String type,        String name    ) {
        this.staffId = staffId;
        this.type = type;
        this.name = name;
    }


    public String getStaffid() {
        return staffId;
    }

    public void setStaffid(String staffId) {
        this.staffId = staffId;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}