





import java.util.List;
import java.util.ArrayList;

public class builds_BuildParameterDefinition extends ParameterDefinition {

    private String buildPlanId;





    private builds_BuildPlan builds_buildplan;


    public builds_BuildParameterDefinition(
        String buildPlanId    ) {
        super(
        );
        this.buildPlanId = buildPlanId;
    }


    public String getBuildplanid() {
        return buildPlanId;
    }

    public void setBuildplanid(String buildPlanId) {
        this.buildPlanId = buildPlanId;
    }

    public builds_BuildPlan getBuilds_buildplan() {
        return builds_buildplan;
    }

    public void setBuilds_buildplan(builds_BuildPlan builds_buildplan) {
        this.builds_buildplan = builds_buildplan;
    }

}