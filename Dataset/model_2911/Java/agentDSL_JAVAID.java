





import java.util.List;
import java.util.ArrayList;

public class agentDSL_JAVAID  {

    private String name;





    private agentDSL_TypeDef agentdsl_typedef;


    public agentDSL_JAVAID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public agentDSL_TypeDef getAgentdsl_typedef() {
        return agentdsl_typedef;
    }

    public void setAgentdsl_typedef(agentDSL_TypeDef agentdsl_typedef) {
        this.agentdsl_typedef = agentdsl_typedef;
    }

}