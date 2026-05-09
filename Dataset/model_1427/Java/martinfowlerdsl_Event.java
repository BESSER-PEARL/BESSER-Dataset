





import java.util.List;
import java.util.ArrayList;

public class martinfowlerdsl_Event extends AbstractEvent {

    private boolean resetting;





    private martinfowlerdsl_Transition martinfowlerdsl_transition;


    public martinfowlerdsl_Event(
        boolean resetting    ) {
        super(
        );
        this.resetting = resetting;
    }


    public boolean getResetting() {
        return resetting;
    }

    public void setResetting(boolean resetting) {
        this.resetting = resetting;
    }

    public martinfowlerdsl_Transition getMartinfowlerdsl_transition() {
        return martinfowlerdsl_transition;
    }

    public void setMartinfowlerdsl_transition(martinfowlerdsl_Transition martinfowlerdsl_transition) {
        this.martinfowlerdsl_transition = martinfowlerdsl_transition;
    }

}