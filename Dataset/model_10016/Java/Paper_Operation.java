





import java.util.List;
import java.util.ArrayList;

public class Paper_Operation  {






    private Paper_Permission paper_permission;




    private List<Paper_Permission> paper_permissions;


    public Paper_Operation(
    ) {
        this.paper_permissions = new ArrayList<>();
    }

    public Paper_Operation(
        ArrayList<Paper_Permission> paper_permissions    ) {
        this.paper_permissions = paper_permissions;
    }


    public Paper_Permission getPaper_permission() {
        return paper_permission;
    }

    public void setPaper_permission(Paper_Permission paper_permission) {
        this.paper_permission = paper_permission;
    }
    public List<Paper_Permission> getPaper_permissions() {
        return paper_permissions;
    }

    public void addPaper_permission(Paper_permission paper_permission) {
        this.paper_permissions.add(paper_permission);
    }

}