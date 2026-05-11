





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_seff_pc_pc_AcquireAction extends AbstractInternalControlFlowAction {

    private float timeoutValue;
    private boolean timeout;





    private PassiveResource passiveresource;


    public pcm_pc_pc_seff_pc_pc_AcquireAction(
        float timeoutValue,        boolean timeout    ) {
        super(
        );
        this.timeoutValue = timeoutValue;
        this.timeout = timeout;
    }


    public float getTimeoutvalue() {
        return timeoutValue;
    }

    public void setTimeoutvalue(float timeoutValue) {
        this.timeoutValue = timeoutValue;
    }
    public boolean getTimeout() {
        return timeout;
    }

    public void setTimeout(boolean timeout) {
        this.timeout = timeout;
    }

    public PassiveResource getPassiveresource() {
        return passiveresource;
    }

    public void setPassiveresource(PassiveResource passiveresource) {
        this.passiveresource = passiveresource;
    }

}