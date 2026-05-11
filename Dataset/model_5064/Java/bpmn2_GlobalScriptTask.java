





import java.util.List;
import java.util.ArrayList;

public class bpmn2_GlobalScriptTask extends GlobalTask {

    private String scriptLanguage;
    private String script;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_GlobalScriptTask(
        String scriptLanguage,        String script    ) {
        super(
        );
        this.scriptLanguage = scriptLanguage;
        this.script = script;
    }


    public String getScriptlanguage() {
        return scriptLanguage;
    }

    public void setScriptlanguage(String scriptLanguage) {
        this.scriptLanguage = scriptLanguage;
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