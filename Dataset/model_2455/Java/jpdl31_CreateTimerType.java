





import java.util.List;
import java.util.ArrayList;

public class jpdl31_CreateTimerType  {

    private String name;
    private String repeat;
    private String transition;
    private String duedate;





    private jpdl31_ActionType jpdl31_actiontype;


    public jpdl31_CreateTimerType(
        String name,        String repeat,        String transition,        String duedate    ) {
        this.name = name;
        this.repeat = repeat;
        this.transition = transition;
        this.duedate = duedate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRepeat() {
        return repeat;
    }

    public void setRepeat(String repeat) {
        this.repeat = repeat;
    }
    public String getTransition() {
        return transition;
    }

    public void setTransition(String transition) {
        this.transition = transition;
    }
    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }

    public jpdl31_ActionType getJpdl31_actiontype() {
        return jpdl31_actiontype;
    }

    public void setJpdl31_actiontype(jpdl31_ActionType jpdl31_actiontype) {
        this.jpdl31_actiontype = jpdl31_actiontype;
    }

}