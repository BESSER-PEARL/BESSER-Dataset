





import java.util.List;
import java.util.ArrayList;

public class aggregator_EnabledStatusProvider  {

    private boolean branchEnabled;
    private boolean enabled;



    public aggregator_EnabledStatusProvider(
        boolean branchEnabled,        boolean enabled    ) {
        this.branchEnabled = branchEnabled;
        this.enabled = enabled;
    }


    public boolean getBranchenabled() {
        return branchEnabled;
    }

    public void setBranchenabled(boolean branchEnabled) {
        this.branchEnabled = branchEnabled;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }


}