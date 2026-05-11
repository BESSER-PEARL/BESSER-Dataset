





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ScriptTask extends Task {

    private String script;
    private String scriptFormat;





    private BPMNProfile_OpaqueAction bpmnprofile_opaqueaction;


    public BPMNProfile_ScriptTask(
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

    public BPMNProfile_OpaqueAction getBpmnprofile_opaqueaction() {
        return bpmnprofile_opaqueaction;
    }

    public void setBpmnprofile_opaqueaction(BPMNProfile_OpaqueAction bpmnprofile_opaqueaction) {
        this.bpmnprofile_opaqueaction = bpmnprofile_opaqueaction;
    }

}