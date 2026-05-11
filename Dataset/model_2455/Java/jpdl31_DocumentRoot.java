





import java.util.List;
import java.util.ArrayList;

public class jpdl31_DocumentRoot  {

    private String mixed;





    private List<jpdl31_DecisionType> jpdl31_decisiontypes;




    private List<jpdl31_Delegation> jpdl31_delegations;




    private List<jpdl31_AssignmentType> jpdl31_assignmenttypes;




    private List<jpdl31_CreateTimerType> jpdl31_createtimertypes;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private List<jpdl31_ActionType> jpdl31_actiontypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_CancelTimerType> jpdl31_canceltimertypes;


    public jpdl31_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.jpdl31_decisiontypes = new ArrayList<>();
        this.jpdl31_delegations = new ArrayList<>();
        this.jpdl31_assignmenttypes = new ArrayList<>();
        this.jpdl31_createtimertypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_actiontypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_canceltimertypes = new ArrayList<>();
    }

    public jpdl31_DocumentRoot(
        String mixed        ArrayList<jpdl31_DecisionType> jpdl31_decisiontypes,        ArrayList<jpdl31_Delegation> jpdl31_delegations,        ArrayList<jpdl31_AssignmentType> jpdl31_assignmenttypes,        ArrayList<jpdl31_CreateTimerType> jpdl31_createtimertypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_ActionType> jpdl31_actiontypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_CancelTimerType> jpdl31_canceltimertypes    ) {
        this.mixed = mixed;
        this.jpdl31_decisiontypes = jpdl31_decisiontypes;
        this.jpdl31_delegations = jpdl31_delegations;
        this.jpdl31_assignmenttypes = jpdl31_assignmenttypes;
        this.jpdl31_createtimertypes = jpdl31_createtimertypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_canceltimertypes = jpdl31_canceltimertypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<jpdl31_DecisionType> getJpdl31_decisiontypes() {
        return jpdl31_decisiontypes;
    }

    public void addJpdl31_decisiontype(Jpdl31_decisiontype jpdl31_decisiontype) {
        this.jpdl31_decisiontypes.add(jpdl31_decisiontype);
    }
    public List<jpdl31_Delegation> getJpdl31_delegations() {
        return jpdl31_delegations;
    }

    public void addJpdl31_delegation(Jpdl31_delegation jpdl31_delegation) {
        this.jpdl31_delegations.add(jpdl31_delegation);
    }
    public List<jpdl31_AssignmentType> getJpdl31_assignmenttypes() {
        return jpdl31_assignmenttypes;
    }

    public void addJpdl31_assignmenttype(Jpdl31_assignmenttype jpdl31_assignmenttype) {
        this.jpdl31_assignmenttypes.add(jpdl31_assignmenttype);
    }
    public List<jpdl31_CreateTimerType> getJpdl31_createtimertypes() {
        return jpdl31_createtimertypes;
    }

    public void addJpdl31_createtimertype(Jpdl31_createtimertype jpdl31_createtimertype) {
        this.jpdl31_createtimertypes.add(jpdl31_createtimertype);
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }
    public List<jpdl31_ExceptionHandlerType> getJpdl31_exceptionhandlertypes() {
        return jpdl31_exceptionhandlertypes;
    }

    public void addJpdl31_exceptionhandlertype(Jpdl31_exceptionhandlertype jpdl31_exceptionhandlertype) {
        this.jpdl31_exceptionhandlertypes.add(jpdl31_exceptionhandlertype);
    }
    public List<jpdl31_CancelTimerType> getJpdl31_canceltimertypes() {
        return jpdl31_canceltimertypes;
    }

    public void addJpdl31_canceltimertype(Jpdl31_canceltimertype jpdl31_canceltimertype) {
        this.jpdl31_canceltimertypes.add(jpdl31_canceltimertype);
    }

}