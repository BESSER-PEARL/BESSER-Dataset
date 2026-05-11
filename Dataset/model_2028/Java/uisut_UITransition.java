





import java.util.List;
import java.util.ArrayList;

public class uisut_UITransition extends UISUTElement {

    private String scriptStr;
    private String actionStr;
    private String guardStr;
    private String triggerStr;





    private uisut_AbstractState uisut_abstractstate;




    private uisut_Action uisut_action;




    private uisut_AbstractState uisut_abstractstate;




    private List<uisut_UIDataVariable> uisut_uidatavariables;




    private uisut_AbstractState uisut_abstractstate;




    private uisut_AbstractState uisut_abstractstate;


    public uisut_UITransition(
        String scriptStr,        String actionStr,        String guardStr,        String triggerStr    ) {
        super(
        );
        this.scriptStr = scriptStr;
        this.actionStr = actionStr;
        this.guardStr = guardStr;
        this.triggerStr = triggerStr;
        this.uisut_uidatavariables = new ArrayList<>();
    }

    public uisut_UITransition(
        String scriptStr,        String actionStr,        String guardStr,        String triggerStr        ArrayList<uisut_UIDataVariable> uisut_uidatavariables    ) {
        this.scriptStr = scriptStr;
        this.actionStr = actionStr;
        this.guardStr = guardStr;
        this.triggerStr = triggerStr;
        this.uisut_uidatavariables = uisut_uidatavariables;
    }

    public String getScriptstr() {
        return scriptStr;
    }

    public void setScriptstr(String scriptStr) {
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

    public uisut_AbstractState getUisut_abstractstate() {
        return uisut_abstractstate;
    }

    public void setUisut_abstractstate(uisut_AbstractState uisut_abstractstate) {
        this.uisut_abstractstate = uisut_abstractstate;
    }
    public uisut_Action getUisut_action() {
        return uisut_action;
    }

    public void setUisut_action(uisut_Action uisut_action) {
        this.uisut_action = uisut_action;
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

}