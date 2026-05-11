





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_MemberSearchCriteria  {

    private String activityGroups;
    private String subDivisions;
    private String divisions;





    private List<Organization> organizations;


    public org_sgiusa_model_MemberSearchCriteria(
        String activityGroups,        String subDivisions,        String divisions    ) {
        this.activityGroups = activityGroups;
        this.subDivisions = subDivisions;
        this.divisions = divisions;
        this.organizations = new ArrayList<>();
    }

    public org_sgiusa_model_MemberSearchCriteria(
        String activityGroups,        String subDivisions,        String divisions        ArrayList<Organization> organizations    ) {
        this.activityGroups = activityGroups;
        this.subDivisions = subDivisions;
        this.divisions = divisions;
        this.organizations = organizations;
    }

    public String getActivitygroups() {
        return activityGroups;
    }

    public void setActivitygroups(String activityGroups) {
        this.activityGroups = activityGroups;
    }
    public String getSubdivisions() {
        return subDivisions;
    }

    public void setSubdivisions(String subDivisions) {
        this.subDivisions = subDivisions;
    }
    public String getDivisions() {
        return divisions;
    }

    public void setDivisions(String divisions) {
        this.divisions = divisions;
    }

    public List<Organization> getOrganizations() {
        return organizations;
    }

    public void addOrganization(Organization organization) {
        this.organizations.add(organization);
    }

}