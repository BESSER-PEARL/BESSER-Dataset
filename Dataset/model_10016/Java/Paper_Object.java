





import java.util.List;
import java.util.ArrayList;

public class Paper_Object  {

    private int ObjID;





    private Paper_Location paper_location;




    private Paper_Permission paper_permission;




    private Paper_Location paper_location;




    private List<Paper_Permission> paper_permissions;


    public Paper_Object(
        int ObjID    ) {
        this.ObjID = ObjID;
        this.paper_permissions = new ArrayList<>();
    }

    public Paper_Object(
        int ObjID        ArrayList<Paper_Permission> paper_permissions    ) {
        this.ObjID = ObjID;
        this.paper_permissions = paper_permissions;
    }

    public int getObjid() {
        return ObjID;
    }

    public void setObjid(int ObjID) {
        this.ObjID = ObjID;
    }

    public Paper_Location getPaper_location() {
        return paper_location;
    }

    public void setPaper_location(Paper_Location paper_location) {
        this.paper_location = paper_location;
    }
    public Paper_Permission getPaper_permission() {
        return paper_permission;
    }

    public void setPaper_permission(Paper_Permission paper_permission) {
        this.paper_permission = paper_permission;
    }
    public Paper_Location getPaper_location() {
        return paper_location;
    }

    public void setPaper_location(Paper_Location paper_location) {
        this.paper_location = paper_location;
    }
    public List<Paper_Permission> getPaper_permissions() {
        return paper_permissions;
    }

    public void addPaper_permission(Paper_permission paper_permission) {
        this.paper_permissions.add(paper_permission);
    }

}