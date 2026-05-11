





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_GlobalScriptTask extends GlobalTask {

    private String scriptFormat;
    private String script;



    public bpmnprof_GlobalScriptTask(
        String scriptFormat,        String script    ) {
        super(
        );
        this.scriptFormat = scriptFormat;
        this.script = script;
    }


    public String getScriptformat() {
        return scriptFormat;
    }

    public void setScriptformat(String scriptFormat) {
        this.scriptFormat = scriptFormat;
    }
    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }


}