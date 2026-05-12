





import java.util.List;
import java.util.ArrayList;

public class Paper_Role  {

    private String RoleName;





    private Paper_User paper_user;




    private List<Paper_User> paper_users;


    public Paper_Role(
        String RoleName    ) {
        this.RoleName = RoleName;
        this.paper_users = new ArrayList<>();
    }

    public Paper_Role(
        String RoleName        ArrayList<Paper_User> paper_users    ) {
        this.RoleName = RoleName;
        this.paper_users = paper_users;
    }

    public String getRolename() {
        return RoleName;
    }

    public void setRolename(String RoleName) {
        this.RoleName = RoleName;
    }

    public Paper_User getPaper_user() {
        return paper_user;
    }

    public void setPaper_user(Paper_User paper_user) {
        this.paper_user = paper_user;
    }
    public List<Paper_User> getPaper_users() {
        return paper_users;
    }

    public void addPaper_user(Paper_user paper_user) {
        this.paper_users.add(paper_user);
    }

}