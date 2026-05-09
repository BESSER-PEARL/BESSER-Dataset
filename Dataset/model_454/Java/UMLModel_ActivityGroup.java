





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ActivityGroup extends Element {

    private String superGroup;
    private String inActivity;
    private String subgroup;





    private List<UMLModel_ActivityEdge> umlmodel_activityedges;


    public UMLModel_ActivityGroup(
        String superGroup,        String inActivity,        String subgroup    ) {
        super(
        );
        this.superGroup = superGroup;
        this.inActivity = inActivity;
        this.subgroup = subgroup;
        this.umlmodel_activityedges = new ArrayList<>();
    }

    public UMLModel_ActivityGroup(
        String superGroup,        String inActivity,        String subgroup        ArrayList<UMLModel_ActivityEdge> umlmodel_activityedges    ) {
        this.superGroup = superGroup;
        this.inActivity = inActivity;
        this.subgroup = subgroup;
        this.umlmodel_activityedges = umlmodel_activityedges;
    }

    public String getSupergroup() {
        return superGroup;
    }

    public void setSupergroup(String superGroup) {
        this.superGroup = superGroup;
    }
    public String getInactivity() {
        return inActivity;
    }

    public void setInactivity(String inActivity) {
        this.inActivity = inActivity;
    }
    public String getSubgroup() {
        return subgroup;
    }

    public void setSubgroup(String subgroup) {
        this.subgroup = subgroup;
    }

    public List<UMLModel_ActivityEdge> getUmlmodel_activityedges() {
        return umlmodel_activityedges;
    }

    public void addUmlmodel_activityedge(Umlmodel_activityedge umlmodel_activityedge) {
        this.umlmodel_activityedges.add(umlmodel_activityedge);
    }

}