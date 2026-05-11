





import java.util.List;
import java.util.ArrayList;

public class projectPlanning_Project  {

    private int requiresResources;
    private String name;





    private List<projectPlanning_Capability> projectplanning_capabilitys;




    private projectPlanning_ProjectPlan projectplanning_projectplan;


    public projectPlanning_Project(
        int requiresResources,        String name    ) {
        this.requiresResources = requiresResources;
        this.name = name;
        this.projectplanning_capabilitys = new ArrayList<>();
    }

    public projectPlanning_Project(
        int requiresResources,        String name        ArrayList<projectPlanning_Capability> projectplanning_capabilitys    ) {
        this.requiresResources = requiresResources;
        this.name = name;
        this.projectplanning_capabilitys = projectplanning_capabilitys;
    }

    public int getRequiresresources() {
        return requiresResources;
    }

    public void setRequiresresources(int requiresResources) {
        this.requiresResources = requiresResources;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<projectPlanning_Capability> getProjectplanning_capabilitys() {
        return projectplanning_capabilitys;
    }

    public void addProjectplanning_capability(Projectplanning_capability projectplanning_capability) {
        this.projectplanning_capabilitys.add(projectplanning_capability);
    }
    public projectPlanning_ProjectPlan getProjectplanning_projectplan() {
        return projectplanning_projectplan;
    }

    public void setProjectplanning_projectplan(projectPlanning_ProjectPlan projectplanning_projectplan) {
        this.projectplanning_projectplan = projectplanning_projectplan;
    }

}