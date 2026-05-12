





import java.util.List;
import java.util.ArrayList;

public class stateMachineActions_Assignment  {

    private String leftvar;





    private stateMachineActions_Action statemachineactions_action;


    public stateMachineActions_Assignment(
        String leftvar    ) {
        this.leftvar = leftvar;
    }


    public String getLeftvar() {
        return leftvar;
    }

    public void setLeftvar(String leftvar) {
        this.leftvar = leftvar;
    }

    public stateMachineActions_Action getStatemachineactions_action() {
        return statemachineactions_action;
    }

    public void setStatemachineactions_action(stateMachineActions_Action statemachineactions_action) {
        this.statemachineactions_action = statemachineactions_action;
    }

}