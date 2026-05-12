





import java.util.List;
import java.util.ArrayList;

public class Paper_Session  {

    private int MaxRoles;





    private Paper_Role paper_role;




    private Paper_User paper_user;




    private Paper_User paper_user;




    private List<Paper_Role> paper_roles;


    public Paper_Session(
        int MaxRoles    ) {
        this.MaxRoles = MaxRoles;
        this.paper_roles = new ArrayList<>();
    }

    public Paper_Session(
        int MaxRoles        ArrayList<Paper_Role> paper_roles    ) {
        this.MaxRoles = MaxRoles;
        this.paper_roles = paper_roles;
    }

    public int getMaxroles() {
        return MaxRoles;
    }

    public void setMaxroles(int MaxRoles) {
        this.MaxRoles = MaxRoles;
    }

    public Paper_Role getPaper_role() {
        return paper_role;
    }

    public void setPaper_role(Paper_Role paper_role) {
        this.paper_role = paper_role;
    }
    public Paper_User getPaper_user() {
        return paper_user;
    }

    public void setPaper_user(Paper_User paper_user) {
        this.paper_user = paper_user;
    }
    public Paper_User getPaper_user() {
        return paper_user;
    }

    public void setPaper_user(Paper_User paper_user) {
        this.paper_user = paper_user;
    }
    public List<Paper_Role> getPaper_roles() {
        return paper_roles;
    }

    public void addPaper_role(Paper_role paper_role) {
        this.paper_roles.add(paper_role);
    }

}