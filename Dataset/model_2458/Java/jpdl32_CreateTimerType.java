





import java.util.List;
import java.util.ArrayList;

public class jpdl32_CreateTimerType  {

    private String transition;
    private String repeat;
    private String name;
    private String duedate;





    private jpdl32_ActionType jpdl32_actiontype;




    private jpdl32_ScriptType jpdl32_scripttype;


    public jpdl32_CreateTimerType(
        String transition,        String repeat,        String name,        String duedate    ) {
        this.transition = transition;
        this.repeat = repeat;
        this.name = name;
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
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }

    public jpdl32_ActionType getJpdl32_actiontype() {
        return jpdl32_actiontype;
    }

    public void setJpdl32_actiontype(jpdl32_ActionType jpdl32_actiontype) {
        this.jpdl32_actiontype = jpdl32_actiontype;
    }
    public jpdl32_ScriptType getJpdl32_scripttype() {
        return jpdl32_scripttype;
    }

    public void setJpdl32_scripttype(jpdl32_ScriptType jpdl32_scripttype) {
        this.jpdl32_scripttype = jpdl32_scripttype;
    }

}