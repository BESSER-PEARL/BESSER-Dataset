





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ScriptTask extends Task {

    private String scriptFormat;
    private String script;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_ScriptTask(
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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}