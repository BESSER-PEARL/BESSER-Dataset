





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_Action  {

    private int duration;
    private String action;
    private int value;





    private missionsDSL_Mission missionsdsl_mission;




    private missionsDSL_Condition missionsdsl_condition;


    public missionsDSL_Action(
        int duration,        String action,        int value    ) {
        this.duration = duration;
        this.action = action;
        this.value = value;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public missionsDSL_Mission getMissionsdsl_mission() {
        return missionsdsl_mission;
    }

    public void setMissionsdsl_mission(missionsDSL_Mission missionsdsl_mission) {
        this.missionsdsl_mission = missionsdsl_mission;
    }
    public missionsDSL_Condition getMissionsdsl_condition() {
        return missionsdsl_condition;
    }

    public void setMissionsdsl_condition(missionsDSL_Condition missionsdsl_condition) {
        this.missionsdsl_condition = missionsdsl_condition;
    }

}