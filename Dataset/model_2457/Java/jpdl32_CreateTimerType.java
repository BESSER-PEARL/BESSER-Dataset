





import java.util.List;
import java.util.ArrayList;

public class jpdl32_CreateTimerType  {

    private String name;
    private String repeat;
    private String duedate;
    private String transition;



    public jpdl32_CreateTimerType(
        String name,        String repeat,        String duedate,        String transition    ) {
        this.name = name;
        this.repeat = repeat;
        this.duedate = duedate;
        this.transition = transition;
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


}