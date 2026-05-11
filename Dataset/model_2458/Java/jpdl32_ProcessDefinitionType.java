





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ProcessDefinitionType  {

    private String group;
    private String name;
    private String description;





    private List<jpdl32_CancelTimerType> jpdl32_canceltimertypes;




    private List<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes;




    private List<jpdl32_MailType> jpdl32_mailtypes;




    private List<jpdl32_DecisionType> jpdl32_decisiontypes;




    private List<jpdl32_CreateTimerType> jpdl32_createtimertypes;




    private List<jpdl32_MailNodeType> jpdl32_mailnodetypes;




    private List<jpdl32_EndStateType> jpdl32_endstatetypes;




    private List<jpdl32_ForkType> jpdl32_forktypes;




    private List<jpdl32_EventType> jpdl32_eventtypes;




    private List<jpdl32_NodeType> jpdl32_nodetypes;




    private List<jpdl32_TaskType> jpdl32_tasktypes;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private List<jpdl32_JoinType> jpdl32_jointypes;




    private List<jpdl32_ScriptType> jpdl32_scripttypes;




    private List<jpdl32_ActionType> jpdl32_actiontypes;


    public jpdl32_ProcessDefinitionType(
        String group,        String name,        String description    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.jpdl32_canceltimertypes = new ArrayList<>();
        this.jpdl32_exceptionhandlertypes = new ArrayList<>();
        this.jpdl32_mailtypes = new ArrayList<>();
        this.jpdl32_decisiontypes = new ArrayList<>();
        this.jpdl32_createtimertypes = new ArrayList<>();
        this.jpdl32_mailnodetypes = new ArrayList<>();
        this.jpdl32_endstatetypes = new ArrayList<>();
        this.jpdl32_forktypes = new ArrayList<>();
        this.jpdl32_eventtypes = new ArrayList<>();
        this.jpdl32_nodetypes = new ArrayList<>();
        this.jpdl32_tasktypes = new ArrayList<>();
        this.jpdl32_jointypes = new ArrayList<>();
        this.jpdl32_scripttypes = new ArrayList<>();
        this.jpdl32_actiontypes = new ArrayList<>();
    }

    public jpdl32_ProcessDefinitionType(
        String group,        String name,        String description        ArrayList<jpdl32_CancelTimerType> jpdl32_canceltimertypes,        ArrayList<jpdl32_ExceptionHandlerType> jpdl32_exceptionhandlertypes,        ArrayList<jpdl32_MailType> jpdl32_mailtypes,        ArrayList<jpdl32_DecisionType> jpdl32_decisiontypes,        ArrayList<jpdl32_CreateTimerType> jpdl32_createtimertypes,        ArrayList<jpdl32_MailNodeType> jpdl32_mailnodetypes,        ArrayList<jpdl32_EndStateType> jpdl32_endstatetypes,        ArrayList<jpdl32_ForkType> jpdl32_forktypes,        ArrayList<jpdl32_EventType> jpdl32_eventtypes,        ArrayList<jpdl32_NodeType> jpdl32_nodetypes,        ArrayList<jpdl32_TaskType> jpdl32_tasktypes,        ArrayList<jpdl32_JoinType> jpdl32_jointypes,        ArrayList<jpdl32_ScriptType> jpdl32_scripttypes,        ArrayList<jpdl32_ActionType> jpdl32_actiontypes    ) {
        this.group = group;
        this.name = name;
        this.description = description;
        this.jpdl32_canceltimertypes = jpdl32_canceltimertypes;
        this.jpdl32_exceptionhandlertypes = jpdl32_exceptionhandlertypes;
        this.jpdl32_mailtypes = jpdl32_mailtypes;
        this.jpdl32_decisiontypes = jpdl32_decisiontypes;
        this.jpdl32_createtimertypes = jpdl32_createtimertypes;
        this.jpdl32_mailnodetypes = jpdl32_mailnodetypes;
        this.jpdl32_endstatetypes = jpdl32_endstatetypes;
        this.jpdl32_forktypes = jpdl32_forktypes;
        this.jpdl32_eventtypes = jpdl32_eventtypes;
        this.jpdl32_nodetypes = jpdl32_nodetypes;
        this.jpdl32_tasktypes = jpdl32_tasktypes;
        this.jpdl32_jointypes = jpdl32_jointypes;
        this.jpdl32_scripttypes = jpdl32_scripttypes;
        this.jpdl32_actiontypes = jpdl32_actiontypes;
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

    public List<jpdl32_CancelTimerType> getJpdl32_canceltimertypes() {
        return jpdl32_canceltimertypes;
    }

    public void addJpdl32_canceltimertype(Jpdl32_canceltimertype jpdl32_canceltimertype) {
        this.jpdl32_canceltimertypes.add(jpdl32_canceltimertype);
    }
    public List<jpdl32_ExceptionHandlerType> getJpdl32_exceptionhandlertypes() {
        return jpdl32_exceptionhandlertypes;
    }

    public void addJpdl32_exceptionhandlertype(Jpdl32_exceptionhandlertype jpdl32_exceptionhandlertype) {
        this.jpdl32_exceptionhandlertypes.add(jpdl32_exceptionhandlertype);
    }
    public List<jpdl32_MailType> getJpdl32_mailtypes() {
        return jpdl32_mailtypes;
    }

    public void addJpdl32_mailtype(Jpdl32_mailtype jpdl32_mailtype) {
        this.jpdl32_mailtypes.add(jpdl32_mailtype);
    }
    public List<jpdl32_DecisionType> getJpdl32_decisiontypes() {
        return jpdl32_decisiontypes;
    }

    public void addJpdl32_decisiontype(Jpdl32_decisiontype jpdl32_decisiontype) {
        this.jpdl32_decisiontypes.add(jpdl32_decisiontype);
    }
    public List<jpdl32_CreateTimerType> getJpdl32_createtimertypes() {
        return jpdl32_createtimertypes;
    }

    public void addJpdl32_createtimertype(Jpdl32_createtimertype jpdl32_createtimertype) {
        this.jpdl32_createtimertypes.add(jpdl32_createtimertype);
    }
    public List<jpdl32_MailNodeType> getJpdl32_mailnodetypes() {
        return jpdl32_mailnodetypes;
    }

    public void addJpdl32_mailnodetype(Jpdl32_mailnodetype jpdl32_mailnodetype) {
        this.jpdl32_mailnodetypes.add(jpdl32_mailnodetype);
    }
    public List<jpdl32_EndStateType> getJpdl32_endstatetypes() {
        return jpdl32_endstatetypes;
    }

    public void addJpdl32_endstatetype(Jpdl32_endstatetype jpdl32_endstatetype) {
        this.jpdl32_endstatetypes.add(jpdl32_endstatetype);
    }
    public List<jpdl32_ForkType> getJpdl32_forktypes() {
        return jpdl32_forktypes;
    }

    public void addJpdl32_forktype(Jpdl32_forktype jpdl32_forktype) {
        this.jpdl32_forktypes.add(jpdl32_forktype);
    }
    public List<jpdl32_EventType> getJpdl32_eventtypes() {
        return jpdl32_eventtypes;
    }

    public void addJpdl32_eventtype(Jpdl32_eventtype jpdl32_eventtype) {
        this.jpdl32_eventtypes.add(jpdl32_eventtype);
    }
    public List<jpdl32_NodeType> getJpdl32_nodetypes() {
        return jpdl32_nodetypes;
    }

    public void addJpdl32_nodetype(Jpdl32_nodetype jpdl32_nodetype) {
        this.jpdl32_nodetypes.add(jpdl32_nodetype);
    }
    public List<jpdl32_TaskType> getJpdl32_tasktypes() {
        return jpdl32_tasktypes;
    }

    public void addJpdl32_tasktype(Jpdl32_tasktype jpdl32_tasktype) {
        this.jpdl32_tasktypes.add(jpdl32_tasktype);
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public List<jpdl32_JoinType> getJpdl32_jointypes() {
        return jpdl32_jointypes;
    }

    public void addJpdl32_jointype(Jpdl32_jointype jpdl32_jointype) {
        this.jpdl32_jointypes.add(jpdl32_jointype);
    }
    public List<jpdl32_ScriptType> getJpdl32_scripttypes() {
        return jpdl32_scripttypes;
    }

    public void addJpdl32_scripttype(Jpdl32_scripttype jpdl32_scripttype) {
        this.jpdl32_scripttypes.add(jpdl32_scripttype);
    }
    public List<jpdl32_ActionType> getJpdl32_actiontypes() {
        return jpdl32_actiontypes;
    }

    public void addJpdl32_actiontype(Jpdl32_actiontype jpdl32_actiontype) {
        this.jpdl32_actiontypes.add(jpdl32_actiontype);
    }

}