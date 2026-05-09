





import java.util.List;
import java.util.ArrayList;

public class traces_Trace  {

    private String rule;





    private traces_TraceSet traces_traceset;


    public traces_Trace(
        String rule    ) {
        this.rule = rule;
    }


    public String getRule() {
        return rule;
    }

    public void setRule(String rule) {
        this.rule = rule;
    }

    public traces_TraceSet getTraces_traceset() {
        return traces_traceset;
    }

    public void setTraces_traceset(traces_TraceSet traces_traceset) {
        this.traces_traceset = traces_traceset;
    }

}