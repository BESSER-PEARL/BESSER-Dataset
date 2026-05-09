





import java.util.List;
import java.util.ArrayList;

public class traces_Trace  {

    private String timestamp;
    private String ruleName;
    private String ruleInfo;





    private traces_TraceRecord traces_tracerecord;


    public traces_Trace(
        String timestamp,        String ruleName,        String ruleInfo    ) {
        this.timestamp = timestamp;
        this.ruleName = ruleName;
        this.ruleInfo = ruleInfo;
    }


    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getRulename() {
        return ruleName;
    }

    public void setRulename(String ruleName) {
        this.ruleName = ruleName;
    }
    public String getRuleinfo() {
        return ruleInfo;
    }

    public void setRuleinfo(String ruleInfo) {
        this.ruleInfo = ruleInfo;
    }

    public traces_TraceRecord getTraces_tracerecord() {
        return traces_tracerecord;
    }

    public void setTraces_tracerecord(traces_TraceRecord traces_tracerecord) {
        this.traces_tracerecord = traces_tracerecord;
    }

}