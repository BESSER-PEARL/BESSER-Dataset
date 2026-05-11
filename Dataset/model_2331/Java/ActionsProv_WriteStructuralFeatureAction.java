





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_WriteStructuralFeatureAction extends StructuralFeatureAction {






    private ActionsProv_OutputPin actionsprov_outputpin;




    private ActionsProv_InputPin actionsprov_inputpin;


    public ActionsProv_WriteStructuralFeatureAction(
    ) {
        super(
        );
    }



    public ActionsProv_OutputPin getActionsprov_outputpin() {
        return actionsprov_outputpin;
    }

    public void setActionsprov_outputpin(ActionsProv_OutputPin actionsprov_outputpin) {
        this.actionsprov_outputpin = actionsprov_outputpin;
    }
    public ActionsProv_InputPin getActionsprov_inputpin() {
        return actionsprov_inputpin;
    }

    public void setActionsprov_inputpin(ActionsProv_InputPin actionsprov_inputpin) {
        this.actionsprov_inputpin = actionsprov_inputpin;
    }

}