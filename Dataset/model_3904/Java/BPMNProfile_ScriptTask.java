





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ScriptTask extends Task {

    private String scriptFormat;
    private String script;



    public BPMNProfile_ScriptTask(
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