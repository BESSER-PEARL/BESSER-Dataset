





import java.util.List;
import java.util.ArrayList;

public class graphbt_RequirementList  {

    private String projectId;





    private List<graphbt_Requirement> graphbt_requirements;


    public graphbt_RequirementList(
        String projectId    ) {
        this.projectId = projectId;
        this.graphbt_requirements = new ArrayList<>();
    }

    public graphbt_RequirementList(
        String projectId        ArrayList<graphbt_Requirement> graphbt_requirements    ) {
        this.projectId = projectId;
        this.graphbt_requirements = graphbt_requirements;
    }

    public String getProjectid() {
        return projectId;
    }

    public void setProjectid(String projectId) {
        this.projectId = projectId;
    }

    public List<graphbt_Requirement> getGraphbt_requirements() {
        return graphbt_requirements;
    }

    public void addGraphbt_requirement(Graphbt_requirement graphbt_requirement) {
        this.graphbt_requirements.add(graphbt_requirement);
    }

}