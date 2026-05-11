





import java.util.List;
import java.util.ArrayList;

public class simulink_Decision  {

    private String actionReference;
    private int id;





    private simulink_ConditionTable simulink_conditiontable;


    public simulink_Decision(
        String actionReference,        int id    ) {
        this.actionReference = actionReference;
        this.id = id;
    }


    public String getActionreference() {
        return actionReference;
    }

    public void setActionreference(String actionReference) {
        this.actionReference = actionReference;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public simulink_ConditionTable getSimulink_conditiontable() {
        return simulink_conditiontable;
    }

    public void setSimulink_conditiontable(simulink_ConditionTable simulink_conditiontable) {
        this.simulink_conditiontable = simulink_conditiontable;
    }

}