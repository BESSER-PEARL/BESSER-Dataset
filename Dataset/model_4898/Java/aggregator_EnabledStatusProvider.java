





import java.util.List;
import java.util.ArrayList;

public class aggregator_EnabledStatusProvider  {

    private boolean enabled;
    private boolean branchEnabled;



    public aggregator_EnabledStatusProvider(
        boolean enabled,        boolean branchEnabled    ) {
        this.enabled = enabled;
        this.branchEnabled = branchEnabled;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public boolean getBranchenabled() {
        return branchEnabled;
    }

    public void setBranchenabled(boolean branchEnabled) {
        this.branchEnabled = branchEnabled;
    }


}