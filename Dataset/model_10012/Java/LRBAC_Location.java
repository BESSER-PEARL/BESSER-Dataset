





import java.util.List;
import java.util.ArrayList;

public class LRBAC_Location  {

    private String LocName;





    private LRBAC_User lrbac_user;




    private List<LRBAC_User> lrbac_users;




    private LRBAC_Role lrbac_role;




    private List<LRBAC_Role> lrbac_roles;


    public LRBAC_Location(
        String LocName    ) {
        this.LocName = LocName;
        this.lrbac_users = new ArrayList<>();
        this.lrbac_roles = new ArrayList<>();
    }

    public LRBAC_Location(
        String LocName        ArrayList<LRBAC_User> lrbac_users,        ArrayList<LRBAC_Role> lrbac_roles    ) {
        this.LocName = LocName;
        this.lrbac_users = lrbac_users;
        this.lrbac_roles = lrbac_roles;
    }

    public String getLocname() {
        return LocName;
    }

    public void setLocname(String LocName) {
        this.LocName = LocName;
    }

    public LRBAC_User getLrbac_user() {
        return lrbac_user;
    }

    public void setLrbac_user(LRBAC_User lrbac_user) {
        this.lrbac_user = lrbac_user;
    }
    public List<LRBAC_User> getLrbac_users() {
        return lrbac_users;
    }

    public void addLrbac_user(Lrbac_user lrbac_user) {
        this.lrbac_users.add(lrbac_user);
    }
    public LRBAC_Role getLrbac_role() {
        return lrbac_role;
    }

    public void setLrbac_role(LRBAC_Role lrbac_role) {
        this.lrbac_role = lrbac_role;
    }
    public List<LRBAC_Role> getLrbac_roles() {
        return lrbac_roles;
    }

    public void addLrbac_role(Lrbac_role lrbac_role) {
        this.lrbac_roles.add(lrbac_role);
    }

}