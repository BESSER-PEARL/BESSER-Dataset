





import java.util.List;
import java.util.ArrayList;

public class jpdl32_ReminderType  {

    private String duedate;
    private String repeat;





    private jpdl32_TaskType jpdl32_tasktype;


    public jpdl32_ReminderType(
        String duedate,        String repeat    ) {
        this.duedate = duedate;
        this.repeat = repeat;
    }


    public String getDuedate() {
        return duedate;
    }

    public void setDuedate(String duedate) {
        this.duedate = duedate;
    }
    public String getRepeat() {
        return repeat;
    }

    public void setRepeat(String repeat) {
        this.repeat = repeat;
    }

    public jpdl32_TaskType getJpdl32_tasktype() {
        return jpdl32_tasktype;
    }

    public void setJpdl32_tasktype(jpdl32_TaskType jpdl32_tasktype) {
        this.jpdl32_tasktype = jpdl32_tasktype;
    }

}