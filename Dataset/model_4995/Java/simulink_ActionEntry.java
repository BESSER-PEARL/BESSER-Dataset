





import java.util.List;
import java.util.ArrayList;

public class simulink_ActionEntry  {

    private String actionStatement;
    private String description;
    private String actionReference;





    private simulink_ActionTable simulink_actiontable;


    public simulink_ActionEntry(
        String actionStatement,        String description,        String actionReference    ) {
        this.actionStatement = actionStatement;
        this.description = description;
        this.actionReference = actionReference;
    }


    public String getActionstatement() {
        return actionStatement;
    }

    public void setActionstatement(String actionStatement) {
        this.actionStatement = actionStatement;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getActionreference() {
        return actionReference;
    }

    public void setActionreference(String actionReference) {
        this.actionReference = actionReference;
    }

    public simulink_ActionTable getSimulink_actiontable() {
        return simulink_actiontable;
    }

    public void setSimulink_actiontable(simulink_ActionTable simulink_actiontable) {
        this.simulink_actiontable = simulink_actiontable;
    }

}