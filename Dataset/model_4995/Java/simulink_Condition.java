





import java.util.List;
import java.util.ArrayList;

public class simulink_Condition  {

    private String statement;
    private String description;





    private simulink_ConditionTable simulink_conditiontable;


    public simulink_Condition(
        String statement,        String description    ) {
        this.statement = statement;
        this.description = description;
    }


    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public simulink_ConditionTable getSimulink_conditiontable() {
        return simulink_conditiontable;
    }

    public void setSimulink_conditiontable(simulink_ConditionTable simulink_conditiontable) {
        this.simulink_conditiontable = simulink_conditiontable;
    }

}