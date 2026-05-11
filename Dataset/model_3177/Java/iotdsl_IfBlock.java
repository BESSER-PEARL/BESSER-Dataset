





import java.util.List;
import java.util.ArrayList;

public class iotdsl_IfBlock  {






    private iotdsl_IfStatement iotdsl_ifstatement;




    private List<iotdsl_Action> iotdsl_actions;




    private iotdsl_IfStatement iotdsl_ifstatement;


    public iotdsl_IfBlock(
    ) {
        this.iotdsl_actions = new ArrayList<>();
    }

    public iotdsl_IfBlock(
        ArrayList<iotdsl_Action> iotdsl_actions    ) {
        this.iotdsl_actions = iotdsl_actions;
    }


    public iotdsl_IfStatement getIotdsl_ifstatement() {
        return iotdsl_ifstatement;
    }

    public void setIotdsl_ifstatement(iotdsl_IfStatement iotdsl_ifstatement) {
        this.iotdsl_ifstatement = iotdsl_ifstatement;
    }
    public List<iotdsl_Action> getIotdsl_actions() {
        return iotdsl_actions;
    }

    public void addIotdsl_action(Iotdsl_action iotdsl_action) {
        this.iotdsl_actions.add(iotdsl_action);
    }
    public iotdsl_IfStatement getIotdsl_ifstatement() {
        return iotdsl_ifstatement;
    }

    public void setIotdsl_ifstatement(iotdsl_IfStatement iotdsl_ifstatement) {
        this.iotdsl_ifstatement = iotdsl_ifstatement;
    }

}