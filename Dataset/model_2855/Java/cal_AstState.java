





import java.util.List;
import java.util.ArrayList;

public class cal_AstState  {

    private String node;
    private String name;





    private cal_ScheduleFsm cal_schedulefsm;


    public cal_AstState(
        String node,        String name    ) {
        this.node = node;
        this.name = name;
    }


    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_ScheduleFsm getCal_schedulefsm() {
        return cal_schedulefsm;
    }

    public void setCal_schedulefsm(cal_ScheduleFsm cal_schedulefsm) {
        this.cal_schedulefsm = cal_schedulefsm;
    }

}