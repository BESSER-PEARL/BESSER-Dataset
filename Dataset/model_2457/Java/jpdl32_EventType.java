





import java.util.List;
import java.util.ArrayList;

public class jpdl32_EventType  {

    private String actionElements;
    private String type;





    private List<jpdl32_ScriptType> jpdl32_scripttypes;




    private List<jpdl32_CreateTimerType> jpdl32_createtimertypes;




    private List<jpdl32_CancelTimerType> jpdl32_canceltimertypes;




    private jpdl32_DecisionType jpdl32_decisiontype;


    public jpdl32_EventType(
        String actionElements,        String type    ) {
        this.actionElements = actionElements;
        this.type = type;
        this.jpdl32_scripttypes = new ArrayList<>();
        this.jpdl32_createtimertypes = new ArrayList<>();
        this.jpdl32_canceltimertypes = new ArrayList<>();
    }

    public jpdl32_EventType(
        String actionElements,        String type        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes,        ArrayList<jpdl32_CreateTimerType> jpdl32_createtimertypes,        ArrayList<jpdl32_CancelTimerType> jpdl32_canceltimertypes    ) {
        this.actionElements = actionElements;
        this.type = type;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
        this.jpdl32_createtimertypes = jpdl32_createtimertypes;
        this.jpdl32_canceltimertypes = jpdl32_canceltimertypes;
    }

    public String getActionelements() {
        return actionElements;
    }

    public void setActionelements(String actionElements) {
        this.actionElements = actionElements;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }
    public List<jpdl32_CreateTimerType> getJpdl32_createtimertypes() {
        return jpdl32_createtimertypes;
    }

    public void addJpdl32_createtimertype(Jpdl32_createtimertype jpdl32_createtimertype) {
        this.jpdl32_createtimertypes.add(jpdl32_createtimertype);
    }
    public List<jpdl32_CancelTimerType> getJpdl32_canceltimertypes() {
        return jpdl32_canceltimertypes;
    }

    public void addJpdl32_canceltimertype(Jpdl32_canceltimertype jpdl32_canceltimertype) {
        this.jpdl32_canceltimertypes.add(jpdl32_canceltimertype);
    }
    public jpdl32_DecisionType getJpdl32_decisiontype() {
        return jpdl32_decisiontype;
    }

    public void setJpdl32_decisiontype(jpdl32_DecisionType jpdl32_decisiontype) {
        this.jpdl32_decisiontype = jpdl32_decisiontype;
    }

}