





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_NewMissions  {






    private missionsDSL_Mission missionsdsl_mission;




    private List<missionsDSL_Mission> missionsdsl_missions;


    public missionsDSL_NewMissions(
    ) {
        this.missionsdsl_missions = new ArrayList<>();
    }

    public missionsDSL_NewMissions(
        ArrayList<missionsDSL_Mission> missionsdsl_missions    ) {
        this.missionsdsl_missions = missionsdsl_missions;
    }


    public missionsDSL_Mission getMissionsdsl_mission() {
        return missionsdsl_mission;
    }

    public void setMissionsdsl_mission(missionsDSL_Mission missionsdsl_mission) {
        this.missionsdsl_mission = missionsdsl_mission;
    }
    public List<missionsDSL_Mission> getMissionsdsl_missions() {
        return missionsdsl_missions;
    }

    public void addMissionsdsl_mission(Missionsdsl_mission missionsdsl_mission) {
        this.missionsdsl_missions.add(missionsdsl_mission);
    }

}