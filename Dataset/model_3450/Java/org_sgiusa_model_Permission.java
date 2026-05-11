





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Permission  {

    private String userId;
    private String enabled;
    private String divisions;
    private String activityGroups;
    private String id;
    private String subDivisions;
    private String capabilities;





    private Organization organization;


    public org_sgiusa_model_Permission(
        String userId,        String enabled,        String divisions,        String activityGroups,        String id,        String subDivisions,        String capabilities    ) {
        this.userId = userId;
        this.enabled = enabled;
        this.divisions = divisions;
        this.activityGroups = activityGroups;
        this.id = id;
        this.subDivisions = subDivisions;
        this.capabilities = capabilities;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSubdivisions() {
        return subDivisions;
    }

    public void setSubdivisions(String subDivisions) {
        this.subDivisions = subDivisions;
    }
    public String getCapabilities() {
        return capabilities;
    }

    public void setCapabilities(String capabilities) {
        this.capabilities = capabilities;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}