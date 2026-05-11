





import java.util.List;
import java.util.ArrayList;

public class application_Source extends ConfigurableElement {

    private String state;
    private String removeDataOnStop;
    private String activeState;
    private String bundleId;
    private String updateRound;
    private String logLevel;



    public application_Source(
        String state,        String removeDataOnStop,        String activeState,        String bundleId,        String updateRound,        String logLevel    ) {
        super(
        );
        this.state = state;
        this.removeDataOnStop = removeDataOnStop;
        this.activeState = activeState;
        this.bundleId = bundleId;
        this.updateRound = updateRound;
        this.logLevel = logLevel;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getRemovedataonstop() {
        return removeDataOnStop;
    }

    public void setRemovedataonstop(String removeDataOnStop) {
        this.removeDataOnStop = removeDataOnStop;
    }
    public String getActivestate() {
        return activeState;
    }

    public void setActivestate(String activeState) {
        this.activeState = activeState;
    }
    public String getBundleid() {
        return bundleId;
    }

    public void setBundleid(String bundleId) {
        this.bundleId = bundleId;
    }
    public String getUpdateround() {
        return updateRound;
    }

    public void setUpdateround(String updateRound) {
        this.updateRound = updateRound;
    }
    public String getLoglevel() {
        return logLevel;
    }

    public void setLoglevel(String logLevel) {
        this.logLevel = logLevel;
    }


}