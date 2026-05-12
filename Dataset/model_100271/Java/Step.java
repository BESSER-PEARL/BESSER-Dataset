





import java.util.List;
import java.util.ArrayList;

public class Step  {






    private Grafcet_TransitionToStep grafcet_transitiontostep;




    private Grafcet_StepToTransition grafcet_steptotransition;


    public Step(
    ) {
    }



    public Grafcet_TransitionToStep getGrafcet_transitiontostep() {
        return grafcet_transitiontostep;
    }

    public void setGrafcet_transitiontostep(Grafcet_TransitionToStep grafcet_transitiontostep) {
        this.grafcet_transitiontostep = grafcet_transitiontostep;
    }
    public Grafcet_StepToTransition getGrafcet_steptotransition() {
        return grafcet_steptotransition;
    }

    public void setGrafcet_steptotransition(Grafcet_StepToTransition grafcet_steptotransition) {
        this.grafcet_steptotransition = grafcet_steptotransition;
    }

}