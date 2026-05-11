





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ScriptTask extends Task {

    private String script;
    private String scriptFormat;



    public bpmn2_ScriptTask(
        String script,        String scriptFormat    ) {
        super(
        );
        this.script = script;
        this.scriptFormat = scriptFormat;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }
    public String getScriptformat() {
        return scriptFormat;
    }

    public void setScriptformat(String scriptFormat) {
        this.scriptFormat = scriptFormat;
    }


}