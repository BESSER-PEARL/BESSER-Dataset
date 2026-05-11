





import java.util.List;
import java.util.ArrayList;

public class simulink_DecisionEntry  {

    private String conditionOutcome;





    private simulink_Decision simulink_decision;




    private simulink_Condition simulink_condition;


    public simulink_DecisionEntry(
        String conditionOutcome    ) {
        this.conditionOutcome = conditionOutcome;
    }


    public String getConditionoutcome() {
        return conditionOutcome;
    }

    public void setConditionoutcome(String conditionOutcome) {
        this.conditionOutcome = conditionOutcome;
    }

    public simulink_Decision getSimulink_decision() {
        return simulink_decision;
    }

    public void setSimulink_decision(simulink_Decision simulink_decision) {
        this.simulink_decision = simulink_decision;
    }
    public simulink_Condition getSimulink_condition() {
        return simulink_condition;
    }

    public void setSimulink_condition(simulink_Condition simulink_condition) {
        this.simulink_condition = simulink_condition;
    }

}