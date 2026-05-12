





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private String Description;
    private String RoleName;
    private int RoleID;
    private boolean isActive;





    private User user;


    public Role(
        String Description,        String RoleName,        int RoleID,        boolean isActive    ) {
        this.Description = Description;
        this.RoleName = RoleName;
        this.RoleID = RoleID;
        this.isActive = isActive;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getRolename() {
        return RoleName;
    }

    public void setRolename(String RoleName) {
        this.RoleName = RoleName;
    }
    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}