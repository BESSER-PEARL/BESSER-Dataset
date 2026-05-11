





import java.util.List;
import java.util.ArrayList;

public class jpdl31_TransitionType  {

    private String to;
    private String group;
    private String name;





    private jpdl31_StateType jpdl31_statetype;




    private jpdl31_TaskNodeType jpdl31_tasknodetype;




    private List<jpdl31_CancelTimerType> jpdl31_canceltimertypes;




    private jpdl31_StartStateType jpdl31_startstatetype;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private List<jpdl31_CreateTimerType> jpdl31_createtimertypes;




    private List<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes;




    private List<jpdl31_ActionType> jpdl31_actiontypes;




    private jpdl31_ProcessStateType jpdl31_processstatetype;




    private jpdl31_ForkType jpdl31_forktype;




    private jpdl31_NodeType jpdl31_nodetype;




    private jpdl31_JoinType jpdl31_jointype;




    private List<jpdl31_ScriptType> jpdl31_scripttypes;




    private jpdl31_SuperStateType jpdl31_superstatetype;


    public jpdl31_TransitionType(
        String to,        String group,        String name    ) {
        this.to = to;
        this.group = group;
        this.name = name;
        this.jpdl31_canceltimertypes = new ArrayList<>();
        this.jpdl31_createtimertypes = new ArrayList<>();
        this.jpdl31_exceptionhandlertypes = new ArrayList<>();
        this.jpdl31_actiontypes = new ArrayList<>();
        this.jpdl31_scripttypes = new ArrayList<>();
    }

    public jpdl31_TransitionType(
        String to,        String group,        String name        ArrayList<jpdl31_CancelTimerType> jpdl31_canceltimertypes,        ArrayList<jpdl31_CreateTimerType> jpdl31_createtimertypes,        ArrayList<jpdl31_ExceptionHandlerType> jpdl31_exceptionhandlertypes,        ArrayList<jpdl31_ActionType> jpdl31_actiontypes,        ArrayList<jpdl31_ScriptType> jpdl31_scripttypes    ) {
        this.to = to;
        this.group = group;
        this.name = name;
        this.jpdl31_canceltimertypes = jpdl31_canceltimertypes;
        this.jpdl31_createtimertypes = jpdl31_createtimertypes;
        this.jpdl31_exceptionhandlertypes = jpdl31_exceptionhandlertypes;
        this.jpdl31_actiontypes = jpdl31_actiontypes;
        this.jpdl31_scripttypes = jpdl31_scripttypes;
    }

    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
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

    public jpdl31_StateType getJpdl31_statetype() {
        return jpdl31_statetype;
    }

    public void setJpdl31_statetype(jpdl31_StateType jpdl31_statetype) {
        this.jpdl31_statetype = jpdl31_statetype;
    }
    public jpdl31_TaskNodeType getJpdl31_tasknodetype() {
        return jpdl31_tasknodetype;
    }

    public void setJpdl31_tasknodetype(jpdl31_TaskNodeType jpdl31_tasknodetype) {
        this.jpdl31_tasknodetype = jpdl31_tasknodetype;
    }
    public List<jpdl31_CancelTimerType> getJpdl31_canceltimertypes() {
        return jpdl31_canceltimertypes;
    }

    public void addJpdl31_canceltimertype(Jpdl31_canceltimertype jpdl31_canceltimertype) {
        this.jpdl31_canceltimertypes.add(jpdl31_canceltimertype);
    }
    public jpdl31_StartStateType getJpdl31_startstatetype() {
        return jpdl31_startstatetype;
    }

    public void setJpdl31_startstatetype(jpdl31_StartStateType jpdl31_startstatetype) {
        this.jpdl31_startstatetype = jpdl31_startstatetype;
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
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
    public List<jpdl31_ActionType> getJpdl31_actiontypes() {
        return jpdl31_actiontypes;
    }

    public void addJpdl31_actiontype(Jpdl31_actiontype jpdl31_actiontype) {
        this.jpdl31_actiontypes.add(jpdl31_actiontype);
    }
    public jpdl31_ProcessStateType getJpdl31_processstatetype() {
        return jpdl31_processstatetype;
    }

    public void setJpdl31_processstatetype(jpdl31_ProcessStateType jpdl31_processstatetype) {
        this.jpdl31_processstatetype = jpdl31_processstatetype;
    }
    public jpdl31_ForkType getJpdl31_forktype() {
        return jpdl31_forktype;
    }

    public void setJpdl31_forktype(jpdl31_ForkType jpdl31_forktype) {
        this.jpdl31_forktype = jpdl31_forktype;
    }
    public jpdl31_NodeType getJpdl31_nodetype() {
        return jpdl31_nodetype;
    }

    public void setJpdl31_nodetype(jpdl31_NodeType jpdl31_nodetype) {
        this.jpdl31_nodetype = jpdl31_nodetype;
    }
    public jpdl31_JoinType getJpdl31_jointype() {
        return jpdl31_jointype;
    }

    public void setJpdl31_jointype(jpdl31_JoinType jpdl31_jointype) {
        this.jpdl31_jointype = jpdl31_jointype;
    }
    public List<jpdl31_ScriptType> getJpdl31_scripttypes() {
        return jpdl31_scripttypes;
    }

    public void addJpdl31_scripttype(Jpdl31_scripttype jpdl31_scripttype) {
        this.jpdl31_scripttypes.add(jpdl31_scripttype);
    }
    public jpdl31_SuperStateType getJpdl31_superstatetype() {
        return jpdl31_superstatetype;
    }

    public void setJpdl31_superstatetype(jpdl31_SuperStateType jpdl31_superstatetype) {
        this.jpdl31_superstatetype = jpdl31_superstatetype;
    }

}