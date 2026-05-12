





import java.util.List;
import java.util.ArrayList;

public class HSM_Transition extends MgaObject {

    private String action;
    private String trigger;
    private String guard;
    private String isSync;



    public HSM_Transition(
        String action,        String trigger,        String guard,        String isSync    ) {
        super(
        );
        this.action = action;
        this.trigger = trigger;
        this.guard = guard;
        this.isSync = isSync;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getIssync() {
        return isSync;
    }

    public void setIssync(String isSync) {
        this.isSync = isSync;
    }


}