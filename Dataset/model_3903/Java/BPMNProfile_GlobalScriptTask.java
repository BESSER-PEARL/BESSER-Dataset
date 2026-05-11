





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_GlobalScriptTask extends GlobalTask {

    private String script;
    private String scriptFormat;



    public BPMNProfile_GlobalScriptTask(
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