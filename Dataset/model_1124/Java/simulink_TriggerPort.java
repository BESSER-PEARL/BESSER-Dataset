





import java.util.List;
import java.util.ArrayList;

public class simulink_TriggerPort extends InPortBlock {

    private String triggerInput;



    public simulink_TriggerPort(
        String triggerInput    ) {
        super(
        );
        this.triggerInput = triggerInput;
    }


    public String getTriggerinput() {
        return triggerInput;
    }

    public void setTriggerinput(String triggerInput) {
        this.triggerInput = triggerInput;
    }


}