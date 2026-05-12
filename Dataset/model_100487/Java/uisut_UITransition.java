





import java.util.List;
import java.util.ArrayList;

public class uisut_UITransition extends UISUTElement {

    private String triggerStr;
    private String scriptStr;
    private String guardStr;
    private String actionStr;





    private uisut_AbstractState uisut_abstractstate;




    private uisut_UIStatemachine uisut_uistatemachine;




    private uisut_AbstractState uisut_abstractstate;




    private uisut_AbstractState uisut_abstractstate;




    private uisut_UITrigger uisut_uitrigger;




    private uisut_UICondition uisut_uicondition;




    private uisut_AbstractState uisut_abstractstate;




    private List<uisut_UIDataVariable> uisut_uidatavariables;


    public uisut_UITransition(
        String triggerStr,        String scriptStr,        String guardStr,        String actionStr    ) {
        super(
        );
        this.triggerStr = triggerStr;
        this.scriptStr = scriptStr;
        this.guardStr = guardStr;
        this.actionStr = actionStr;
        this.uisut_uidatavariables = new ArrayList<>();
    }

    public uisut_UITransition(
        String triggerStr,        String scriptStr,        String guardStr,        String actionStr        ArrayList<uisut_UIDataVariable> uisut_uidatavariables    ) {
        this.triggerStr = triggerStr;
        this.scriptStr = scriptStr;
        this.guardStr = guardStr;
        this.actionStr = actionStr;
        this.uisut_uidatavariables = uisut_uidatavariables;
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
    public String getGuardstr() {
        return guardStr;
    }

    public void setGuardstr(String guardStr) {
        this.guardStr = guardStr;
    }
    public String getActionstr() {
        return actionStr;
    }

    public void setActionstr(String actionStr) {
        this.actionStr = actionStr;
    }

    public uisut_AbstractState getUisut_abstractstate() {
        return uisut_abstractstate;
    }

    public void setUisut_abstractstate(uisut_AbstractState uisut_abstractstate) {
        this.uisut_abstractstate = uisut_abstractstate;
    }
    public uisut_UIStatemachine getUisut_uistatemachine() {
        return uisut_uistatemachine;
    }

    public void setUisut_uistatemachine(uisut_UIStatemachine uisut_uistatemachine) {
        this.uisut_uistatemachine = uisut_uistatemachine;
    }
    public uisut_AbstractState getUisut_abstractstate() {
        return uisut_abstractstate;
    }

    public void setUisut_abstractstate(uisut_AbstractState uisut_abstractstate) {
        this.uisut_abstractstate = uisut_abstractstate;
    }
    public uisut_AbstractState getUisut_abstractstate() {
        return uisut_abstractstate;
    }

    public void setUisut_abstractstate(uisut_AbstractState uisut_abstractstate) {
        this.uisut_abstractstate = uisut_abstractstate;
    }
    public uisut_UITrigger getUisut_uitrigger() {
        return uisut_uitrigger;
    }

    public void setUisut_uitrigger(uisut_UITrigger uisut_uitrigger) {
        this.uisut_uitrigger = uisut_uitrigger;
    }
    public uisut_UICondition getUisut_uicondition() {
        return uisut_uicondition;
    }

    public void setUisut_uicondition(uisut_UICondition uisut_uicondition) {
        this.uisut_uicondition = uisut_uicondition;
    }
    public uisut_AbstractState getUisut_abstractstate() {
        return uisut_abstractstate;
    }

    public void setUisut_abstractstate(uisut_AbstractState uisut_abstractstate) {
        this.uisut_abstractstate = uisut_abstractstate;
    }
    public List<uisut_UIDataVariable> getUisut_uidatavariables() {
        return uisut_uidatavariables;
    }

    public void addUisut_uidatavariable(Uisut_uidatavariable uisut_uidatavariable) {
        this.uisut_uidatavariables.add(uisut_uidatavariable);
    }

}