





import java.util.List;
import java.util.ArrayList;

public class bpmn2_GlobalScriptTask extends GlobalTask {

    private String script;
    private String scriptLanguage;



    public bpmn2_GlobalScriptTask(
        String script,        String scriptLanguage    ) {
        super(
        );
        this.script = script;
        this.scriptLanguage = scriptLanguage;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }
    public String getScriptlanguage() {
        return scriptLanguage;
    }

    public void setScriptlanguage(String scriptLanguage) {
        this.scriptLanguage = scriptLanguage;
    }


}