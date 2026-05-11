





import java.util.List;
import java.util.ArrayList;

public class agentDSL_Attribute  {

    private String name;
    private boolean many;





    private agentDSL_Task agentdsl_task;




    private agentDSL_Entity agentdsl_entity;




    private agentDSL_Outcome agentdsl_outcome;




    private agentDSL_Type agentdsl_type;




    private agentDSL_Function agentdsl_function;


    public agentDSL_Attribute(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public agentDSL_Task getAgentdsl_task() {
        return agentdsl_task;
    }

    public void setAgentdsl_task(agentDSL_Task agentdsl_task) {
        this.agentdsl_task = agentdsl_task;
    }
    public agentDSL_Entity getAgentdsl_entity() {
        return agentdsl_entity;
    }

    public void setAgentdsl_entity(agentDSL_Entity agentdsl_entity) {
        this.agentdsl_entity = agentdsl_entity;
    }
    public agentDSL_Outcome getAgentdsl_outcome() {
        return agentdsl_outcome;
    }

    public void setAgentdsl_outcome(agentDSL_Outcome agentdsl_outcome) {
        this.agentdsl_outcome = agentdsl_outcome;
    }
    public agentDSL_Type getAgentdsl_type() {
        return agentdsl_type;
    }

    public void setAgentdsl_type(agentDSL_Type agentdsl_type) {
        this.agentdsl_type = agentdsl_type;
    }
    public agentDSL_Function getAgentdsl_function() {
        return agentdsl_function;
    }

    public void setAgentdsl_function(agentDSL_Function agentdsl_function) {
        this.agentdsl_function = agentdsl_function;
    }

}