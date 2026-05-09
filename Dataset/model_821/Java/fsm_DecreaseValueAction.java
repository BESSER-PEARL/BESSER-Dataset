





import java.util.List;
import java.util.ArrayList;

public class fsm_DecreaseValueAction extends Action {

    private int stepValue;



    public fsm_DecreaseValueAction(
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