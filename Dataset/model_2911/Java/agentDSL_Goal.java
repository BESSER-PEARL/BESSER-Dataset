





import java.util.List;
import java.util.ArrayList;

public class agentDSL_Goal  {

    private String name;





    private agentDSL_Outcome agentdsl_outcome;




    private List<agentDSL_Attribute> agentdsl_attributes;


    public agentDSL_Goal(
        String name    ) {
        this.name = name;
        this.agentdsl_attributes = new ArrayList<>();
    }

    public agentDSL_Goal(
        String name        ArrayList<agentDSL_Attribute> agentdsl_attributes    ) {
        this.name = name;
        this.agentdsl_attributes = agentdsl_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public agentDSL_Outcome getAgentdsl_outcome() {
        return agentdsl_outcome;
    }

    public void setAgentdsl_outcome(agentDSL_Outcome agentdsl_outcome) {
        this.agentdsl_outcome = agentdsl_outcome;
    }
    public List<agentDSL_Attribute> getAgentdsl_attributes() {
        return agentdsl_attributes;
    }

    public void addAgentdsl_attribute(Agentdsl_attribute agentdsl_attribute) {
        this.agentdsl_attributes.add(agentdsl_attribute);
    }

}