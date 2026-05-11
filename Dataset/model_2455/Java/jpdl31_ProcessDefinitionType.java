





import java.util.List;
import java.util.ArrayList;

public class jpdl31_ProcessDefinitionType  {

    private String group;
    private String name;





    private List<jpdl31_EndStateType> jpdl31_endstatetypes;




    private List<jpdl31_DecisionType> jpdl31_decisiontypes;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_NodeType> jpdl31_nodetypes;




    private List<jpdl31_ActionType> jpdl31_actiontypes;




    private List<jpdl31_JoinType> jpdl31_jointypes;




    private List<jpdl31_EventType> jpdl31_eventtypes;




    private List<jpdl31_ProcessStateType> jpdl31_processstatetypes;




    private List<jpdl31_CancelTimerType> jpdl31_canceltimertypes;




    private List<jpdl31_ForkType> jpdl31_forktypes;




    private List<jpdl31_CreateTimerType> jpdl31_createtimertypes;




    private jpdl31_DocumentRoot jpdl31_documentroot;


    public jpdl31_ProcessDefinitionType(
        String group,        String name    ) {
        this.group = group;
        this.name = name;
        this.jpdl31_endstatetypes = new ArrayList<>();
        this.jpdl31_decisiontypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_nodetypes = new ArrayList<>();
        this.jpdl31_actiontypes = new ArrayList<>();
        this.jpdl31_jointypes = new ArrayList<>();
        this.jpdl31_eventtypes = new ArrayList<>();
        this.jpdl31_processstatetypes = new ArrayList<>();
        this.jpdl31_canceltimertypes = new ArrayList<>();
        this.jpdl31_forktypes = new ArrayList<>();
        this.jpdl31_createtimertypes = new ArrayList<>();
    }

    public jpdl31_ProcessDefinitionType(
        String group,        String name        ArrayList<jpdl31_EndStateType> jpdl31_endstatetypes,        ArrayList<jpdl31_DecisionType> jpdl31_decisiontypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_NodeType> jpdl31_nodetypes,        ArrayList<jpdl31_ActionType> jpdl31_actiontypes,        ArrayList<jpdl31_JoinType> jpdl31_jointypes,        ArrayList<jpdl31_EventType> jpdl31_eventtypes,        ArrayList<jpdl31_ProcessStateType> jpdl31_processstatetypes,        ArrayList<jpdl31_CancelTimerType> jpdl31_canceltimertypes,        ArrayList<jpdl31_ForkType> jpdl31_forktypes,        ArrayList<jpdl31_CreateTimerType> jpdl31_createtimertypes    ) {
        this.group = group;
        this.name = name;
        this.jpdl31_endstatetypes = jpdl31_endstatetypes;
        this.jpdl31_decisiontypes = jpdl31_decisiontypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_nodetypes = jpdl31_nodetypes;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
        this.jpdl31_jointypes = jpdl31_jointypes;
        this.jpdl31_eventtypes = jpdl31_eventtypes;
        this.jpdl31_processstatetypes = jpdl31_processstatetypes;
        this.jpdl31_canceltimertypes = jpdl31_canceltimertypes;
        this.jpdl31_forktypes = jpdl31_forktypes;
        this.jpdl31_createtimertypes = jpdl31_createtimertypes;
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

    public List<jpdl31_EndStateType> getJpdl31_endstatetypes() {
        return jpdl31_endstatetypes;
    }

    public void addJpdl31_endstatetype(Jpdl31_endstatetype jpdl31_endstatetype) {
        this.jpdl31_endstatetypes.add(jpdl31_endstatetype);
    }
    public List<jpdl31_DecisionType> getJpdl31_decisiontypes() {
        return jpdl31_decisiontypes;
    }

    public void addJpdl31_decisiontype(Jpdl31_decisiontype jpdl31_decisiontype) {
        this.jpdl31_decisiontypes.add(jpdl31_decisiontype);
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
    public List<jpdl31_NodeType> getJpdl31_nodetypes() {
        return jpdl31_nodetypes;
    }

    public void addJpdl31_nodetype(Jpdl31_nodetype jpdl31_nodetype) {
        this.jpdl31_nodetypes.add(jpdl31_nodetype);
    }
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }
    public List<jpdl31_JoinType> getJpdl31_jointypes() {
        return jpdl31_jointypes;
    }

    public void addJpdl31_jointype(Jpdl31_jointype jpdl31_jointype) {
        this.jpdl31_jointypes.add(jpdl31_jointype);
    }
    public List<jpdl31_EventType> getJpdl31_eventtypes() {
        return jpdl31_eventtypes;
    }

    public void addJpdl31_eventtype(Jpdl31_eventtype jpdl31_eventtype) {
        this.jpdl31_eventtypes.add(jpdl31_eventtype);
    }
    public List<jpdl31_ProcessStateType> getJpdl31_processstatetypes() {
        return jpdl31_processstatetypes;
    }

    public void addJpdl31_processstatetype(Jpdl31_processstatetype jpdl31_processstatetype) {
        this.jpdl31_processstatetypes.add(jpdl31_processstatetype);
    }
    public List<jpdl31_CancelTimerType> getJpdl31_canceltimertypes() {
        return jpdl31_canceltimertypes;
    }

    public void addJpdl31_canceltimertype(Jpdl31_canceltimertype jpdl31_canceltimertype) {
        this.jpdl31_canceltimertypes.add(jpdl31_canceltimertype);
    }
    public List<jpdl31_ForkType> getJpdl31_forktypes() {
        return jpdl31_forktypes;
    }

    public void addJpdl31_forktype(Jpdl31_forktype jpdl31_forktype) {
        this.jpdl31_forktypes.add(jpdl31_forktype);
    }
    public List<jpdl31_CreateTimerType> getJpdl31_createtimertypes() {
        return jpdl31_createtimertypes;
    }

    public void addJpdl31_createtimertype(Jpdl31_createtimertype jpdl31_createtimertype) {
        this.jpdl31_createtimertypes.add(jpdl31_createtimertype);
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }

}