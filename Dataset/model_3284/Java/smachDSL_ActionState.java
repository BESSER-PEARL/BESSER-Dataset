





import java.util.List;
import java.util.ArrayList;

public class smachDSL_ActionState  {

    private String name;





    private smachDSL_ActionClient smachdsl_actionclient;




    private smachDSL_StateMachine smachdsl_statemachine;


    public smachDSL_ActionState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smachDSL_ActionClient getSmachdsl_actionclient() {
        return smachdsl_actionclient;
    }

    public void setSmachdsl_actionclient(smachDSL_ActionClient smachdsl_actionclient) {
        this.smachdsl_actionclient = smachdsl_actionclient;
    }
    public smachDSL_StateMachine getSmachdsl_statemachine() {
        return smachdsl_statemachine;
    }

    public void setSmachdsl_statemachine(smachDSL_StateMachine smachdsl_statemachine) {
        this.smachdsl_statemachine = smachdsl_statemachine;
    }

}