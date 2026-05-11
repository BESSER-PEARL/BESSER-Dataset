





import java.util.List;
import java.util.ArrayList;

public class jpdl32_EventType  {

    private String type;
    private String actionElements;





    private List<jpdl32_ActionType> jpdl32_actiontypes;




    private List<jpdl32_ScriptType> jpdl32_scripttypes;




    private List<jpdl32_CancelTimerType> jpdl32_canceltimertypes;




    private List<jpdl32_CreateTimerType> jpdl32_createtimertypes;




    private jpdl32_DecisionType jpdl32_decisiontype;


    public jpdl32_EventType(
        String type,        String actionElements    ) {
        this.type = type;
        this.actionElements = actionElements;
        this.jpdl32_actiontypes = new ArrayList<>();
        this.jpdl32_scripttypes = new ArrayList<>();
        this.jpdl32_canceltimertypes = new ArrayList<>();
        this.jpdl32_createtimertypes = new ArrayList<>();
    }

    public jpdl32_EventType(
        String type,        String actionElements        ArrayList<jpdl32_ActionType> jpdl32_actiontypes,        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes,        ArrayList<jpdl32_CancelTimerType> jpdl32_canceltimertypes,        ArrayList<jpdl32_CreateTimerType> jpdl32_createtimertypes    ) {
        this.type = type;
        this.actionElements = actionElements;
        this.jpdl32_actiontypes = jpdl32_actiontypes;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
        this.jpdl32_canceltimertypes = jpdl32_canceltimertypes;
        this.jpdl32_createtimertypes = jpdl32_createtimertypes;
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

    public List<jpdl32_ActionType> getJpdl32_actiontypes() {
        return jpdl32_actiontypes;
    }

    public void addJpdl32_actiontype(Jpdl32_actiontype jpdl32_actiontype) {
        this.jpdl32_actiontypes.add(jpdl32_actiontype);
    }
    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }
    public List<jpdl32_CancelTimerType> getJpdl32_canceltimertypes() {
        return jpdl32_canceltimertypes;
    }

    public void addJpdl32_canceltimertype(Jpdl32_canceltimertype jpdl32_canceltimertype) {
        this.jpdl32_canceltimertypes.add(jpdl32_canceltimertype);
    }
    public List<jpdl32_CreateTimerType> getJpdl32_createtimertypes() {
        return jpdl32_createtimertypes;
    }

    public void addJpdl32_createtimertype(Jpdl32_createtimertype jpdl32_createtimertype) {
        this.jpdl32_createtimertypes.add(jpdl32_createtimertype);
    }
    public jpdl32_DecisionType getJpdl32_decisiontype() {
        return jpdl32_decisiontype;
    }

    public void setJpdl32_decisiontype(jpdl32_DecisionType jpdl32_decisiontype) {
        this.jpdl32_decisiontype = jpdl32_decisiontype;
    }

}