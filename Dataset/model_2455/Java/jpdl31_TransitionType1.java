





import java.util.List;
import java.util.ArrayList;

public class jpdl31_TransitionType1  {

    private String group;
    private String name;
    private String to;





    private List<jpdl31_CancelTimerType> jpdl31_canceltimertypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;




    private List<jpdl31_CreateTimerType> jpdl31_createtimertypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_ConditionType> jpdl31_conditiontypes;




    private List<jpdl31_ActionType> jpdl31_actiontypes;




    private jpdl31_DecisionType jpdl31_decisiontype;


    public jpdl31_TransitionType1(
        String group,        String name,        String to    ) {
        this.group = group;
        this.name = name;
        this.to = to;
        this.jpdl31_canceltimertypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
        this.jpdl31_createtimertypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_conditiontypes = new ArrayList<>();
        this.jpdl31_actiontypes = new ArrayList<>();
    }

    public jpdl31_TransitionType1(
        String group,        String name,        String to        ArrayList<jpdl31_CancelTimerType> jpdl31_canceltimertypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes,        ArrayList<jpdl31_CreateTimerType> jpdl31_createtimertypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_ConditionType> jpdl31_conditiontypes,        ArrayList<jpdl31_ActionType> jpdl31_actiontypes    ) {
        this.group = group;
        this.name = name;
        this.to = to;
        this.jpdl31_canceltimertypes = jpdl31_canceltimertypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
        this.jpdl31_createtimertypes = jpdl31_createtimertypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_conditiontypes = jpdl31_conditiontypes;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
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
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public List<jpdl31_CancelTimerType> getJpdl31_canceltimertypes() {
        return jpdl31_canceltimertypes;
    }

    public void addJpdl31_canceltimertype(Jpdl31_canceltimertype jpdl31_canceltimertype) {
        this.jpdl31_canceltimertypes.add(jpdl31_canceltimertype);
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }
    public List<jpdl31_CreateTimerType> getJpdl31_createtimertypes() {
        return jpdl31_createtimertypes;
    }

    public void addJpdl31_createtimertype(Jpdl31_createtimertype jpdl31_createtimertype) {
        this.jpdl31_createtimertypes.add(jpdl31_createtimertype);
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public List<jpdl31_ConditionType> getJpdl31_conditiontypes() {
        return jpdl31_conditiontypes;
    }

    public void addJpdl31_conditiontype(Jpdl31_conditiontype jpdl31_conditiontype) {
        this.jpdl31_conditiontypes.add(jpdl31_conditiontype);
    }
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }
    public jpdl31_DecisionType getJpdl31_decisiontype() {
        return jpdl31_decisiontype;
    }

    public void setJpdl31_decisiontype(jpdl31_DecisionType jpdl31_decisiontype) {
        this.jpdl31_decisiontype = jpdl31_decisiontype;
    }

}