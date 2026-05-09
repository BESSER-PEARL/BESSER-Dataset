





import java.util.List;
import java.util.ArrayList;

public class tfsm_TFSM extends NamedElement {

    private int lastStateChangeStepNumber;
    private int stepNumber;



    public tfsm_TFSM(
        int lastStateChangeStepNumber,        int stepNumber    ) {
        super(
        );
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
        this.stepNumber = stepNumber;
    }


    public int getLaststatechangestepnumber() {
        return lastStateChangeStepNumber;
    }

    public void setLaststatechangestepnumber(int lastStateChangeStepNumber) {
        this.lastStateChangeStepNumber = lastStateChangeStepNumber;
    }
    public int getStepnumber() {
        return stepNumber;
    }

    public void setStepnumber(int stepNumber) {
        this.stepNumber = stepNumber;
    }


}