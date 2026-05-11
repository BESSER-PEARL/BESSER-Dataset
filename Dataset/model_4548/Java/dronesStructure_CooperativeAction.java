





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_CooperativeAction extends NamedElement {

    private float duration;
    private float startTimeout;





    private dronesStructure_DronesStructure dronesstructure_dronesstructure;


    public dronesStructure_CooperativeAction(
        float duration,        float startTimeout    ) {
        super(
        );
        this.duration = duration;
        this.startTimeout = startTimeout;
    }


    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }
    public float getStarttimeout() {
        return startTimeout;
    }

    public void setStarttimeout(float startTimeout) {
        this.startTimeout = startTimeout;
    }

    public dronesStructure_DronesStructure getDronesstructure_dronesstructure() {
        return dronesstructure_dronesstructure;
    }

    public void setDronesstructure_dronesstructure(dronesStructure_DronesStructure dronesstructure_dronesstructure) {
        this.dronesstructure_dronesstructure = dronesstructure_dronesstructure;
    }

}