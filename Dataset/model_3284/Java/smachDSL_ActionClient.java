





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ActionClient  {

    private String name;
    private String actiontype;
    private String actionname;





    private smachDSL_StateMachine smachdsl_statemachine;


    public smachDSL_ActionClient(
        String name,        String actiontype,        String actionname    ) {
        this.name = name;
        this.actiontype = actiontype;
        this.actionname = actionname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }
    public String getActionname() {
        return actionname;
    }

    public void setActionname(String actionname) {
        this.actionname = actionname;
    }

    public smachDSL_StateMachine getSmachdsl_statemachine() {
        return smachdsl_statemachine;
    }

    public void setSmachdsl_statemachine(smachDSL_StateMachine smachdsl_statemachine) {
        this.smachdsl_statemachine = smachdsl_statemachine;
    }

}