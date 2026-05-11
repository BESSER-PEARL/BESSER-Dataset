





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_DebugLog extends ActionStep {

    private String debugLevel;



    public core_actionstep_DebugLog(
        String debugLevel    ) {
        super(
        );
        this.debugLevel = debugLevel;
    }


    public String getDebuglevel() {
        return debugLevel;
    }

    public void setDebuglevel(String debugLevel) {
        this.debugLevel = debugLevel;
    }


}