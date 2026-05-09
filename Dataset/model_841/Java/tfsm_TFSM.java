





import java.util.List;
import java.util.ArrayList;

public class tfsm_TFSM extends NamedElement {

    private int stepNumber;
    private int lastStateChangeStepNumber;



    public tfsm_TFSM(
        int stepNumber,        int lastStateChangeStepNumber    ) {
        super(
        );
        this.stepNumber = stepNumber;
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
    }


    public int getStepnumber() {
        return stepNumber;
    }

    public void setStepnumber(int stepNumber) {
        this.stepNumber = stepNumber;
    }
    public int getLaststatechangestepnumber() {
        return lastStateChangeStepNumber;
    }

    public void setLaststatechangestepnumber(int lastStateChangeStepNumber) {
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
    }


}