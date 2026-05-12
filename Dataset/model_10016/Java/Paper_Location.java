





import java.util.List;
import java.util.ArrayList;

public class Paper_Location  {

    private String LocName;





    private List<Paper_User> paper_users;




    private Paper_User paper_user;




    private Paper_Role paper_role;




    private List<Paper_Role> paper_roles;


    public Paper_Location(
        String LocName    ) {
        this.LocName = LocName;
        this.paper_users = new ArrayList<>();
        this.paper_roles = new ArrayList<>();
    }

    public Paper_Location(
        String LocName        ArrayList<Paper_User> paper_users,        ArrayList<Paper_Role> paper_roles    ) {
        this.LocName = LocName;
        this.paper_users = paper_users;
        this.paper_roles = paper_roles;
    }

    public String getLocname() {
        return LocName;
    }

    public void setLocname(String LocName) {
        this.LocName = LocName;
    }

    public List<Paper_User> getPaper_users() {
        return paper_users;
    }

    public void addPaper_user(Paper_user paper_user) {
        this.paper_users.add(paper_user);
    }
    public Paper_User getPaper_user() {
        return paper_user;
    }

    public void setPaper_user(Paper_User paper_user) {
        this.paper_user = paper_user;
    }
    public Paper_Role getPaper_role() {
        return paper_role;
    }

    public void setPaper_role(Paper_Role paper_role) {
        this.paper_role = paper_role;
    }
    public List<Paper_Role> getPaper_roles() {
        return paper_roles;
    }

    public void addPaper_role(Paper_role paper_role) {
        this.paper_roles.add(paper_role);
    }

}