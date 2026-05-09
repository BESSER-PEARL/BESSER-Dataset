





import java.util.List;
import java.util.ArrayList;

public class fsm_IncreaseValueAction extends Action {

    private int stepValue;



    public fsm_IncreaseValueAction(
        int stepValue    ) {
        super(
        );
        this.stepValue = stepValue;
    }


    public int getStepvalue() {
        return stepValue;
    }

    public void setStepvalue(int stepValue) {
        this.stepValue = stepValue;
    }


}