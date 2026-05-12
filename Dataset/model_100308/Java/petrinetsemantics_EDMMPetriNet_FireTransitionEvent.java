





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_EDMMPetriNet_FireTransitionEvent extends PetriNetEvent {

    private float time;



    public petrinetsemantics_EDMMPetriNet_FireTransitionEvent(
        float time    ) {
        super(
        );
        this.time = time;
    }


    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }


}