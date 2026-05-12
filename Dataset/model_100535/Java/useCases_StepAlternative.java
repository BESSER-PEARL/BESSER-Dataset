





import java.util.List;
import java.util.ArrayList;

public class useCases_StepAlternative  {

    private boolean finalizeFlow;
    private String finalState;





    private useCases_CustomStepType usecases_customsteptype;




    private useCases_Step usecases_step;




    private useCases_Step usecases_step;


    public useCases_StepAlternative(
        boolean finalizeFlow,        String finalState    ) {
        this.finalizeFlow = finalizeFlow;
        this.finalState = finalState;
    }


    public boolean getFinalizeflow() {
        return finalizeFlow;
    }

    public void setFinalizeflow(boolean finalizeFlow) {
        this.finalizeFlow = finalizeFlow;
    }
    public String getFinalstate() {
        return finalState;
    }

    public void setFinalstate(String finalState) {
        this.finalState = finalState;
    }

    public useCases_CustomStepType getUsecases_customsteptype() {
        return usecases_customsteptype;
    }

    public void setUsecases_customsteptype(useCases_CustomStepType usecases_customsteptype) {
        this.usecases_customsteptype = usecases_customsteptype;
    }
    public useCases_Step getUsecases_step() {
        return usecases_step;
    }

    public void setUsecases_step(useCases_Step usecases_step) {
        this.usecases_step = usecases_step;
    }
    public useCases_Step getUsecases_step() {
        return usecases_step;
    }

    public void setUsecases_step(useCases_Step usecases_step) {
        this.usecases_step = usecases_step;
    }

}