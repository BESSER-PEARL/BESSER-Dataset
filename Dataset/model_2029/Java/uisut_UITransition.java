





import java.util.List;
import java.util.ArrayList;

public class uisut_UITransition extends UISUTElement {

    private String actionStr;
    private String guardStr;
    private String triggerStr;
    private String scriptStr;





    private uisut_UITrigger uisut_uitrigger;




    private uisut_Action uisut_action;




    private uisut_UICondition uisut_uicondition;




    private uisut_UIStatemachine uisut_uistatemachine;


    public uisut_UITransition(
        String actionStr,        String guardStr,        String triggerStr,        String scriptStr    ) {
        super(
        );
        this.actionStr = actionStr;
        this.guardStr = guardStr;
        this.triggerStr = triggerStr;
        this.scriptStr = scriptStr;
    }


    public String getActionstr() {
        return actionStr;
    }

    public void setActionstr(String actionStr) {
        this.actionStr = actionStr;
    }
    public String getGuardstr() {
        return guardStr;
    }

    public void setGuardstr(String guardStr) {
        this.guardStr = guardStr;
    }
    public String getTriggerstr() {
        return triggerStr;
    }

    public void setTriggerstr(String triggerStr) {
        this.triggerStr = triggerStr;
    }
    public String getScriptstr() {
        return scriptStr;
    }

    public void setScriptstr(String scriptStr) {
        this.scriptStr = scriptStr;
    }

    public uisut_UITrigger getUisut_uitrigger() {
        return uisut_uitrigger;
    }

    public void setUisut_uitrigger(uisut_UITrigger uisut_uitrigger) {
        this.uisut_uitrigger = uisut_uitrigger;
    }
    public uisut_Action getUisut_action() {
        return uisut_action;
    }

    public void setUisut_action(uisut_Action uisut_action) {
        this.uisut_action = uisut_action;
    }
    public uisut_UICondition getUisut_uicondition() {
        return uisut_uicondition;
    }

    public void setUisut_uicondition(uisut_UICondition uisut_uicondition) {
        this.uisut_uicondition = uisut_uicondition;
    }
    public uisut_UIStatemachine getUisut_uistatemachine() {
        return uisut_uistatemachine;
    }

    public void setUisut_uistatemachine(uisut_UIStatemachine uisut_uistatemachine) {
        this.uisut_uistatemachine = uisut_uistatemachine;
    }

}