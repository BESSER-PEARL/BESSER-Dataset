





import java.util.List;
import java.util.ArrayList;

public class projectPlanning_Capability  {

    private String name;





    private projectPlanning_ProjectPlan projectplanning_projectplan;


    public projectPlanning_Capability(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public projectPlanning_ProjectPlan getProjectplanning_projectplan() {
        return projectplanning_projectplan;
    }

    public void setProjectplanning_projectplan(projectPlanning_ProjectPlan projectplanning_projectplan) {
        this.projectplanning_projectplan = projectplanning_projectplan;
    }

}