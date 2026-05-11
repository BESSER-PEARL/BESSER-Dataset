





import java.util.List;
import java.util.ArrayList;

public class agentDSL_Type  {

    private String name;





    private agentDSL_Model agentdsl_model;


    public agentDSL_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public agentDSL_Model getAgentdsl_model() {
        return agentdsl_model;
    }

    public void setAgentdsl_model(agentDSL_Model agentdsl_model) {
        this.agentdsl_model = agentdsl_model;
    }

}