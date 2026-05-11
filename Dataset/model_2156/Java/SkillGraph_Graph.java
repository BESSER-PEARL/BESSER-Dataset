





import java.util.List;
import java.util.ArrayList;

public class SkillGraph_Graph  {






    private SkillGraph_Parameter skillgraph_parameter;




    private List<SkillGraph_Parameter> skillgraph_parameters;


    public SkillGraph_Graph(
    ) {
        this.skillgraph_parameters = new ArrayList<>();
    }

    public SkillGraph_Graph(
        ArrayList<SkillGraph_Parameter> skillgraph_parameters    ) {
        this.skillgraph_parameters = skillgraph_parameters;
    }


    public SkillGraph_Parameter getSkillgraph_parameter() {
        return skillgraph_parameter;
    }

    public void setSkillgraph_parameter(SkillGraph_Parameter skillgraph_parameter) {
        this.skillgraph_parameter = skillgraph_parameter;
    }
    public List<SkillGraph_Parameter> getSkillgraph_parameters() {
        return skillgraph_parameters;
    }

    public void addSkillgraph_parameter(Skillgraph_parameter skillgraph_parameter) {
        this.skillgraph_parameters.add(skillgraph_parameter);
    }

}