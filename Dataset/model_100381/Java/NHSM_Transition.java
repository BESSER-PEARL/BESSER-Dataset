





import java.util.List;
import java.util.ArrayList;

public class NHSM_Transition  {

    private String trigger;
    private String effect;



    public NHSM_Transition(
        String trigger,        String effect    ) {
        this.trigger = trigger;
        this.effect = effect;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }


}