





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_seff_av_av_AcquireAction extends AbstractInternalControlFlowAction {

    private boolean timeout;
    private float timeoutValue;





    private PassiveResource passiveresource;


    public pcm_av_av_seff_av_av_AcquireAction(
        boolean timeout,        float timeoutValue    ) {
        super(
        );
        this.timeout = timeout;
        this.timeoutValue = timeoutValue;
    }


    public boolean getTimeout() {
        return timeout;
    }

    public void setTimeout(boolean timeout) {
        this.timeout = timeout;
    }
    public float getTimeoutvalue() {
        return timeoutValue;
    }

    public void setTimeoutvalue(float timeoutValue) {
        this.timeoutValue = timeoutValue;
    }

    public PassiveResource getPassiveresource() {
        return passiveresource;
    }

    public void setPassiveresource(PassiveResource passiveresource) {
        this.passiveresource = passiveresource;
    }

}