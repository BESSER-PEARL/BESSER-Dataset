





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_EmailList  {

    private String subDivisions;
    private String id;
    private String divisions;
    private String activityGroups;
    private String enabled;





    private Organization organization;


    public org_sgiusa_model_EmailList(
        String subDivisions,        String id,        String divisions,        String activityGroups,        String enabled    ) {
        this.subDivisions = subDivisions;
        this.id = id;
        this.divisions = divisions;
        this.activityGroups = activityGroups;
        this.enabled = enabled;
    }


    public String getSubdivisions() {
        return subDivisions;
    }

    public void setSubdivisions(String subDivisions) {
        this.subDivisions = subDivisions;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDivisions() {
        return divisions;
    }

    public void setDivisions(String divisions) {
        this.divisions = divisions;
    }
    public String getActivitygroups() {
        return activityGroups;
    }

    public void setActivitygroups(String activityGroups) {
        this.activityGroups = activityGroups;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}