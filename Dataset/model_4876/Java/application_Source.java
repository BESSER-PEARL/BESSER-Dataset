





import java.util.List;
import java.util.ArrayList;

public class application_Source extends ConfigurableElement {

    private String removeDataOnStop;
    private String bundleId;
    private String state;
    private String updateRound;
    private String logLevel;
    private String activeState;



    public application_Source(
        String removeDataOnStop,        String bundleId,        String state,        String updateRound,        String logLevel,        String activeState    ) {
        super(
        );
        this.removeDataOnStop = removeDataOnStop;
        this.bundleId = bundleId;
        this.state = state;
        this.updateRound = updateRound;
        this.logLevel = logLevel;
        this.activeState = activeState;
    }


    public String getRemovedataonstop() {
        return removeDataOnStop;
    }

    public void setRemovedataonstop(String removeDataOnStop) {
        this.removeDataOnStop = removeDataOnStop;
    }
    public String getBundleid() {
        return bundleId;
    }

    public void setBundleid(String bundleId) {
        this.bundleId = bundleId;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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
    public String getActivestate() {
        return activeState;
    }

    public void setActivestate(String activeState) {
        this.activeState = activeState;
    }


}