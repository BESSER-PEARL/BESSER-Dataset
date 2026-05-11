





import java.util.List;
import java.util.ArrayList;

public class uitf_TriggeredTransition extends Statement {

    private String scriptStr;
    private String transitionId;



    public uitf_TriggeredTransition(
        String scriptStr,        String transitionId    ) {
        super(
        );
        this.scriptStr = scriptStr;
        this.transitionId = transitionId;
    }


    public String getScriptstr() {
        return scriptStr;
    }

    public void setScriptstr(String scriptStr) {
        this.scriptStr = scriptStr;
    }
    public String getTransitionid() {
        return transitionId;
    }

    public void setTransitionid(String transitionId) {
        this.transitionId = transitionId;
    }


}