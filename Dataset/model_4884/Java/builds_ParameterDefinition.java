





import java.util.List;
import java.util.ArrayList;

public class builds_ParameterDefinition  {

    private String name;
    private String description;





    private builds_BuildPlan builds_buildplan;




    private builds_BuildPlan builds_buildplan;


    public builds_ParameterDefinition(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }
    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }

}