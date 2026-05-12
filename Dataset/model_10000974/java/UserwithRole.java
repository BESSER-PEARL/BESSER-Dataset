





import java.util.List;
import java.util.ArrayList;

public class UserwithRole  {

    private int RoleId;
    private int UserId;





    private List<Users> userss;




    private List<UserRoles> userroless;


    public UserwithRole(
        int RoleId,        int UserId    ) {
        this.RoleId = RoleId;
        this.UserId = UserId;
        this.userss = new ArrayList<>();
        this.userroless = new ArrayList<>();
    }

    public UserwithRole(
        int RoleId,        int UserId        ArrayList<Users> userss,        ArrayList<UserRoles> userroless    ) {
        this.RoleId = RoleId;
        this.UserId = UserId;
        this.userss = userss;
        this.userroless = userroless;
    }

    public int getRoleid() {
        return RoleId;
    }

    public void setRoleid(int RoleId) {
        this.RoleId = RoleId;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }

    public List<Users> getUserss() {
        return userss;
    }

    public void addUsers(Users users) {
        this.userss.add(users);
    }
    public List<UserRoles> getUserroless() {
        return userroless;
    }

    public void addUserroles(Userroles userroles) {
        this.userroless.add(userroles);
    }

}