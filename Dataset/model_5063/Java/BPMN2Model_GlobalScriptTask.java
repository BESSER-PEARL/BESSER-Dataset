





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_GlobalScriptTask extends GlobalTask {

    private String scriptLanguage;
    private String script;



    public BPMN2Model_GlobalScriptTask(
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


}