





import java.util.List;
import java.util.ArrayList;

public class aadl2_TriggerPort extends ModeTransitionTrigger {






    private aadl2_ModeTransition aadl2_modetransition;




    private aadl2_Context aadl2_context;


    public aadl2_TriggerPort(
    ) {
        super(
        );
    }



    public aadl2_ModeTransition getAadl2_modetransition() {
        return aadl2_modetransition;
    }

    public void setAadl2_modetransition(aadl2_ModeTransition aadl2_modetransition) {
        this.aadl2_modetransition = aadl2_modetransition;
    }
    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }

}