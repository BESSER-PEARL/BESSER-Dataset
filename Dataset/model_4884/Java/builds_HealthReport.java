





import java.util.List;
import java.util.ArrayList;

public class builds_HealthReport  {

    private String description;
    private int health;





    private builds_BuildPlan builds_buildplan;


    public builds_HealthReport(
        String description,        int health    ) {
        this.description = description;
        this.health = health;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }

}