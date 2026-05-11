





import java.util.List;
import java.util.ArrayList;

public class jpdl32_TransitionType  {

    private String group;
    private String name;
    private String description;
    private String to;





    private List<jpdl32_CancelTimerType> jpdl32_canceltimertypes;




    private List<jpdl32_ConditionType> jpdl32_conditiontypes;




    private List<jpdl32_ActionType> jpdl32_actiontypes;




    private jpdl32_DecisionType jpdl32_decisiontype;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_CreateTimerType> jpdl32_createtimertypes;




    private List<jpdl32_ScriptType> jpdl32_scripttypes;


    public jpdl32_TransitionType(
        String group,        String name,        String description,        String to    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.to = to;
        this.jpdl32_canceltimertypes = new ArrayList<>();
        this.jpdl32_conditiontypes = new ArrayList<>();
        this.jpdl32_actiontypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_createtimertypes = new ArrayList<>();
        this.jpdl32_scripttypes = new ArrayList<>();
    }

    public jpdl32_TransitionType(
        String group,        String name,        String description,        String to        ArrayList<jpdl32_CancelTimerType> jpdl32_canceltimertypes,        ArrayList<jpdl32_ConditionType> jpdl32_conditiontypes,        ArrayList<jpdl32_ActionType> jpdl32_actiontypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_CreateTimerType> jpdl32_createtimertypes,        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.to = to;
        this.jpdl32_canceltimertypes = jpdl32_canceltimertypes;
        this.jpdl32_conditiontypes = jpdl32_conditiontypes;
        this.jpdl32_actiontypes = jpdl32_actiontypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_createtimertypes = jpdl32_createtimertypes;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public List<jpdl32_CancelTimerType> getJpdl32_canceltimertypes() {
        return jpdl32_canceltimertypes;
    }

    public void addJpdl32_canceltimertype(Jpdl32_canceltimertype jpdl32_canceltimertype) {
        this.jpdl32_canceltimertypes.add(jpdl32_canceltimertype);
    }
    public List<jpdl32_ConditionType> getJpdl32_conditiontypes() {
        return jpdl32_conditiontypes;
    }

    public void addJpdl32_conditiontype(Jpdl32_conditiontype jpdl32_conditiontype) {
        this.jpdl32_conditiontypes.add(jpdl32_conditiontype);
    }
    public List<jpdl32_ActionType> getJpdl32_actiontypes() {
        return jpdl32_actiontypes;
    }

    public void addJpdl32_actiontype(Jpdl32_actiontype jpdl32_actiontype) {
        this.jpdl32_actiontypes.add(jpdl32_actiontype);
    }
    public jpdl32_DecisionType getJpdl32_decisiontype() {
        return jpdl32_decisiontype;
    }

    public void setJpdl32_decisiontype(jpdl32_DecisionType jpdl32_decisiontype) {
        this.jpdl32_decisiontype = jpdl32_decisiontype;
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_CreateTimerType> getJpdl32_createtimertypes() {
        return jpdl32_createtimertypes;
    }

    public void addJpdl32_createtimertype(Jpdl32_createtimertype jpdl32_createtimertype) {
        this.jpdl32_createtimertypes.add(jpdl32_createtimertype);
    }
    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }

}