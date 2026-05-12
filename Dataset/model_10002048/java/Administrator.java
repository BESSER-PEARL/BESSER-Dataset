





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Name;
    private String adminID;



    public Administrator(
        String Name,        String adminID    ) {
        this.Name = Name;
        this.adminID = adminID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAdminid() {
        return adminID;
    }

    public void setAdminid(String adminID) {
        this.adminID = adminID;
    }


}