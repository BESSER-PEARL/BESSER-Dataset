





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_Condition  {

    private String sensor;
    private String relation;





    private missionsDSL_Mission missionsdsl_mission;


    public missionsDSL_Condition(
        String sensor,        String relation    ) {
        this.sensor = sensor;
        this.relation = relation;
    }


    public String getSensor() {
        return sensor;
    }

    public void setSensor(String sensor) {
        this.sensor = sensor;
    }
    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }

    public missionsDSL_Mission getMissionsdsl_mission() {
        return missionsdsl_mission;
    }

    public void setMissionsdsl_mission(missionsDSL_Mission missionsdsl_mission) {
        this.missionsdsl_mission = missionsdsl_mission;
    }

}