





import java.util.List;
import java.util.ArrayList;

public class jpdl31_TimerType  {

    private String name;
    private String transition;
    private String repeat;
    private String duedate;





    private jpdl31_TaskType jpdl31_tasktype;




    private jpdl31_TaskNodeType jpdl31_tasknodetype;




    private jpdl31_ForkType jpdl31_forktype;




    private jpdl31_NodeType jpdl31_nodetype;




    private jpdl31_ProcessStateType jpdl31_processstatetype;




    private jpdl31_ScriptType jpdl31_scripttype;




    private jpdl31_DocumentRoot jpdl31_documentroot;




    private jpdl31_JoinType jpdl31_jointype;




    private jpdl31_ActionType jpdl31_actiontype;


    public jpdl31_TimerType(
        String name,        String transition,        String repeat,        String duedate    ) {
        this.name = name;
        this.transition = transition;
        this.repeat = repeat;
        this.duedate = duedate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTransition() {
        return transition;
    }

    public void setTransition(String transition) {
        this.transition = transition;
    }
    public String getRepeat() {
        return repeat;
    }

    public void setRepeat(String repeat) {
        this.repeat = repeat;
    }
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }

    public jpdl31_TaskType getJpdl31_tasktype() {
        return jpdl31_tasktype;
    }

    public void setJpdl31_tasktype(jpdl31_TaskType jpdl31_tasktype) {
        this.jpdl31_tasktype = jpdl31_tasktype;
    }
    public jpdl31_TaskNodeType getJpdl31_tasknodetype() {
        return jpdl31_tasknodetype;
    }

    public void setJpdl31_tasknodetype(jpdl31_TaskNodeType jpdl31_tasknodetype) {
        this.jpdl31_tasknodetype = jpdl31_tasknodetype;
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
    public jpdl31_ProcessStateType getJpdl31_processstatetype() {
        return jpdl31_processstatetype;
    }

    public void setJpdl31_processstatetype(jpdl31_ProcessStateType jpdl31_processstatetype) {
        this.jpdl31_processstatetype = jpdl31_processstatetype;
    }
    public jpdl31_ScriptType getJpdl31_scripttype() {
        return jpdl31_scripttype;
    }

    public void setJpdl31_scripttype(jpdl31_ScriptType jpdl31_scripttype) {
        this.jpdl31_scripttype = jpdl31_scripttype;
    }
    public jpdl31_DocumentRoot getJpdl31_documentroot() {
        return jpdl31_documentroot;
    }

    public void setJpdl31_documentroot(jpdl31_DocumentRoot jpdl31_documentroot) {
        this.jpdl31_documentroot = jpdl31_documentroot;
    }
    public jpdl31_JoinType getJpdl31_jointype() {
        return jpdl31_jointype;
    }

    public void setJpdl31_jointype(jpdl31_JoinType jpdl31_jointype) {
        this.jpdl31_jointype = jpdl31_jointype;
    }
    public jpdl31_ActionType getJpdl31_actiontype() {
        return jpdl31_actiontype;
    }

    public void setJpdl31_actiontype(jpdl31_ActionType jpdl31_actiontype) {
        this.jpdl31_actiontype = jpdl31_actiontype;
    }

}