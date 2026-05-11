





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ActionClient  {

    private String actionname;
    private String name;
    private String actiontype;





    private smachDSL_StateMachine smachdsl_statemachine;


    public smachDSL_ActionClient(
        String actionname,        String name,        String actiontype    ) {
        this.actionname = actionname;
        this.name = name;
        this.actiontype = actiontype;
    }


    public String getActionname() {
        return actionname;
    }

    public void setActionname(String actionname) {
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

    public smachDSL_StateMachine getSmachdsl_statemachine() {
        return smachdsl_statemachine;
    }

    public void setSmachdsl_statemachine(smachDSL_StateMachine smachdsl_statemachine) {
        this.smachdsl_statemachine = smachdsl_statemachine;
    }

}