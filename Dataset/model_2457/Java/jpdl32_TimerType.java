





import java.util.List;
import java.util.ArrayList;

public class jpdl32_TimerType  {

    private String duedate;
    private String transition;
    private String repeat;
    private String name;





    private jpdl32_MailType jpdl32_mailtype;




    private jpdl32_CancelTimerType jpdl32_canceltimertype;




    private jpdl32_ForkType jpdl32_forktype;




    private jpdl32_SuperStateType jpdl32_superstatetype;




    private jpdl32_NodeType jpdl32_nodetype;




    private jpdl32_TaskNodeType jpdl32_tasknodetype;




    private jpdl32_ProcessStateType jpdl32_processstatetype;




    private jpdl32_StateType jpdl32_statetype;




    private jpdl32_ScriptType jpdl32_scripttype;




    private jpdl32_JoinType jpdl32_jointype;




    private jpdl32_CreateTimerType jpdl32_createtimertype;




    private jpdl32_DocumentRoot jpdl32_documentroot;




    private jpdl32_MailNodeType jpdl32_mailnodetype;




    private jpdl32_TaskType jpdl32_tasktype;


    public jpdl32_TimerType(
        String duedate,        String transition,        String repeat,        String name    ) {
        this.duedate = duedate;
        this.transition = transition;
        this.repeat = repeat;
        this.name = name;
    }


    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl32_MailType getJpdl32_mailtype() {
        return jpdl32_mailtype;
    }

    public void setJpdl32_mailtype(jpdl32_MailType jpdl32_mailtype) {
        this.jpdl32_mailtype = jpdl32_mailtype;
    }
    public jpdl32_CancelTimerType getJpdl32_canceltimertype() {
        return jpdl32_canceltimertype;
    }

    public void setJpdl32_canceltimertype(jpdl32_CancelTimerType jpdl32_canceltimertype) {
        this.jpdl32_canceltimertype = jpdl32_canceltimertype;
    }
    public jpdl32_ForkType getJpdl32_forktype() {
        return jpdl32_forktype;
    }

    public void setJpdl32_forktype(jpdl32_ForkType jpdl32_forktype) {
        this.jpdl32_forktype = jpdl32_forktype;
    }
    public jpdl32_SuperStateType getJpdl32_superstatetype() {
        return jpdl32_superstatetype;
    }

    public void setJpdl32_superstatetype(jpdl32_SuperStateType jpdl32_superstatetype) {
        this.jpdl32_superstatetype = jpdl32_superstatetype;
    }
    public jpdl32_NodeType getJpdl32_nodetype() {
        return jpdl32_nodetype;
    }

    public void setJpdl32_nodetype(jpdl32_NodeType jpdl32_nodetype) {
        this.jpdl32_nodetype = jpdl32_nodetype;
    }
    public jpdl32_TaskNodeType getJpdl32_tasknodetype() {
        return jpdl32_tasknodetype;
    }

    public void setJpdl32_tasknodetype(jpdl32_TaskNodeType jpdl32_tasknodetype) {
        this.jpdl32_tasknodetype = jpdl32_tasknodetype;
    }
    public jpdl32_ProcessStateType getJpdl32_processstatetype() {
        return jpdl32_processstatetype;
    }

    public void setJpdl32_processstatetype(jpdl32_ProcessStateType jpdl32_processstatetype) {
        this.jpdl32_processstatetype = jpdl32_processstatetype;
    }
    public jpdl32_StateType getJpdl32_statetype() {
        return jpdl32_statetype;
    }

    public void setJpdl32_statetype(jpdl32_StateType jpdl32_statetype) {
        this.jpdl32_statetype = jpdl32_statetype;
    }
    public jpdl32_ScriptType getJpdl32_scripttype() {
        return jpdl32_scripttype;
    }

    public void setJpdl32_scripttype(jpdl32_ScriptType jpdl32_scripttype) {
        this.jpdl32_scripttype = jpdl32_scripttype;
    }
    public jpdl32_JoinType getJpdl32_jointype() {
        return jpdl32_jointype;
    }

    public void setJpdl32_jointype(jpdl32_JoinType jpdl32_jointype) {
        this.jpdl32_jointype = jpdl32_jointype;
    }
    public jpdl32_CreateTimerType getJpdl32_createtimertype() {
        return jpdl32_createtimertype;
    }

    public void setJpdl32_createtimertype(jpdl32_CreateTimerType jpdl32_createtimertype) {
        this.jpdl32_createtimertype = jpdl32_createtimertype;
    }
    public jpdl32_DocumentRoot getJpdl32_documentroot() {
        return jpdl32_documentroot;
    }

    public void setJpdl32_documentroot(jpdl32_DocumentRoot jpdl32_documentroot) {
        this.jpdl32_documentroot = jpdl32_documentroot;
    }
    public jpdl32_MailNodeType getJpdl32_mailnodetype() {
        return jpdl32_mailnodetype;
    }

    public void setJpdl32_mailnodetype(jpdl32_MailNodeType jpdl32_mailnodetype) {
        this.jpdl32_mailnodetype = jpdl32_mailnodetype;
    }
    public jpdl32_TaskType getJpdl32_tasktype() {
        return jpdl32_tasktype;
    }

    public void setJpdl32_tasktype(jpdl32_TaskType jpdl32_tasktype) {
        this.jpdl32_tasktype = jpdl32_tasktype;
    }

}