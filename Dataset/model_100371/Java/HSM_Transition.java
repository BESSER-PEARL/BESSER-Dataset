





import java.util.List;
import java.util.ArrayList;

public class HSM_Transition extends MgaObject {

    private String guard;
    private String trigger;
    private String isSync;
    private String action;



    public HSM_Transition(
        String guard,        String trigger,        String isSync,        String action    ) {
        super(
        );
        this.guard = guard;
        this.trigger = trigger;
        this.isSync = isSync;
        this.action = action;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getIssync() {
        return isSync;
    }

    public void setIssync(String isSync) {
        this.isSync = isSync;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}