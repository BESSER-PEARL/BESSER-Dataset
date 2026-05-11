





import java.util.List;
import java.util.ArrayList;

public class jpdl31_EventType  {

    private String type;
    private String actionElements;





    private List<jpdl31_CreateTimerType> jpdl31_createtimertypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;




    private List<jpdl31_CancelTimerType> jpdl31_canceltimertypes;




    private jpdl31_DecisionType jpdl31_decisiontype;




    private List<jpdl31_ActionType> jpdl31_actiontypes;


    public jpdl31_EventType(
        String type,        String actionElements    ) {
        this.type = type;
        this.actionElements = actionElements;
        this.jpdl31_createtimertypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
        this.jpdl31_canceltimertypes = new ArrayList<>();
        this.jpdl31_actiontypes = new ArrayList<>();
    }

    public jpdl31_EventType(
        String type,        String actionElements        ArrayList<jpdl31_CreateTimerType> jpdl31_createtimertypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes,        ArrayList<jpdl31_CancelTimerType> jpdl31_canceltimertypes,        ArrayList<jpdl31_ActionType> jpdl31_actiontypes    ) {
        this.type = type;
        this.actionElements = actionElements;
        this.jpdl31_createtimertypes = jpdl31_createtimertypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
        this.jpdl31_canceltimertypes = jpdl31_canceltimertypes;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActionelements() {
        return actionElements;
    }

    public void setActionelements(String actionElements) {
        this.actionElements = actionElements;
    }

    public List<jpdl31_CreateTimerType> getJpdl31_createtimertypes() {
        return jpdl31_createtimertypes;
    }

    public void addJpdl31_createtimertype(Jpdl31_createtimertype jpdl31_createtimertype) {
        this.jpdl31_createtimertypes.add(jpdl31_createtimertype);
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }
    public List<jpdl31_CancelTimerType> getJpdl31_canceltimertypes() {
        return jpdl31_canceltimertypes;
    }

    public void addJpdl31_canceltimertype(Jpdl31_canceltimertype jpdl31_canceltimertype) {
        this.jpdl31_canceltimertypes.add(jpdl31_canceltimertype);
    }
    public jpdl31_DecisionType getJpdl31_decisiontype() {
        return jpdl31_decisiontype;
    }

    public void setJpdl31_decisiontype(jpdl31_DecisionType jpdl31_decisiontype) {
        this.jpdl31_decisiontype = jpdl31_decisiontype;
    }
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }

}