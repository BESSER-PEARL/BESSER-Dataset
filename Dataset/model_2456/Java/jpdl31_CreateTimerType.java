





import java.util.List;
import java.util.ArrayList;

public class jpdl31_CreateTimerType  {

    private String transition;
    private String repeat;
    private String duedate;
    private String name;





    private jpdl31_ActionType jpdl31_actiontype;




    private jpdl31_EventType jpdl31_eventtype;




    private jpdl31_ScriptType jpdl31_scripttype;


    public jpdl31_CreateTimerType(
        String transition,        String repeat,        String duedate,        String name    ) {
        this.transition = transition;
        this.repeat = repeat;
        this.duedate = duedate;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl31_ActionType getJpdl31_actiontype() {
        return jpdl31_actiontype;
    }

    public void setJpdl31_actiontype(jpdl31_ActionType jpdl31_actiontype) {
        this.jpdl31_actiontype = jpdl31_actiontype;
    }
    public jpdl31_EventType getJpdl31_eventtype() {
        return jpdl31_eventtype;
    }

    public void setJpdl31_eventtype(jpdl31_EventType jpdl31_eventtype) {
        this.jpdl31_eventtype = jpdl31_eventtype;
    }
    public jpdl31_ScriptType getJpdl31_scripttype() {
        return jpdl31_scripttype;
    }

    public void setJpdl31_scripttype(jpdl31_ScriptType jpdl31_scripttype) {
        this.jpdl31_scripttype = jpdl31_scripttype;
    }

}