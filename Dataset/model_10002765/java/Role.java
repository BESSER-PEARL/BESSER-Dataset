





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private String Description;
    private int RoleID;
    private None Name;



    public Role(
        String Description,        int RoleID,        None Name    ) {
        this.Description = Description;
        this.RoleID = RoleID;
        this.Name = Name;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
    }
    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }


}