





import java.util.List;
import java.util.ArrayList;

public class statemachine103_Transition extends StateMachineObject {

    private String guardExpression;
    private String guardLabel;



    public statemachine103_Transition(
        String guardExpression,        String guardLabel    ) {
        super(
        );
        this.guardExpression = guardExpression;
        this.guardLabel = guardLabel;
    }


    public String getGuardexpression() {
        return guardExpression;
    }

    public void setGuardexpression(String guardExpression) {
        this.guardExpression = guardExpression;
    }
    public String getGuardlabel() {
        return guardLabel;
    }

    public void setGuardlabel(String guardLabel) {
        this.guardLabel = guardLabel;
    }


}