





import java.util.List;
import java.util.ArrayList;

public class dsl_Task  {

    private int nrOfTimes;
    private String name;
    private String action;
    private int time;





    private dsl_Mission dsl_mission;


    public dsl_Task(
        int nrOfTimes,        String name,        String action,        int time    ) {
        this.nrOfTimes = nrOfTimes;
        this.name = name;
        this.action = action;
        this.time = time;
    }


    public int getNroftimes() {
        return nrOfTimes;
    }

    public void setNroftimes(int nrOfTimes) {
        this.nrOfTimes = nrOfTimes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public dsl_Mission getDsl_mission() {
        return dsl_mission;
    }

    public void setDsl_mission(dsl_Mission dsl_mission) {
        this.dsl_mission = dsl_mission;
    }

}