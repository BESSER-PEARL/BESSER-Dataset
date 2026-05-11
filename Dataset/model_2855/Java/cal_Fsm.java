





import java.util.List;
import java.util.ArrayList;

public class cal_Fsm  {






    private List<cal_AstState> cal_aststates;




    private cal_ScheduleFsm cal_schedulefsm;




    private cal_LocalFsm cal_localfsm;


    public cal_Fsm(
    ) {
        this.cal_aststates = new ArrayList<>();
    }

    public cal_Fsm(
        ArrayList<cal_AstState> cal_aststates    ) {
        this.cal_aststates = cal_aststates;
    }


    public List<cal_AstState> getCal_aststates() {
        return cal_aststates;
    }

    public void addCal_aststate(Cal_aststate cal_aststate) {
        this.cal_aststates.add(cal_aststate);
    }
    public cal_ScheduleFsm getCal_schedulefsm() {
        return cal_schedulefsm;
    }

    public void setCal_schedulefsm(cal_ScheduleFsm cal_schedulefsm) {
        this.cal_schedulefsm = cal_schedulefsm;
    }
    public cal_LocalFsm getCal_localfsm() {
        return cal_localfsm;
    }

    public void setCal_localfsm(cal_LocalFsm cal_localfsm) {
        this.cal_localfsm = cal_localfsm;
    }

}