





import java.util.List;
import java.util.ArrayList;

public class missionsDSL_Mission  {

    private String name;
    private int priority;
    private String type;





    private missionsDSL_Robot missionsdsl_robot;




    private missionsDSL_Robot missionsdsl_robot;


    public missionsDSL_Mission(
        String name,        int priority,        String type    ) {
        this.name = name;
        this.priority = priority;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public missionsDSL_Robot getMissionsdsl_robot() {
        return missionsdsl_robot;
    }

    public void setMissionsdsl_robot(missionsDSL_Robot missionsdsl_robot) {
        this.missionsdsl_robot = missionsdsl_robot;
    }
    public missionsDSL_Robot getMissionsdsl_robot() {
        return missionsdsl_robot;
    }

    public void setMissionsdsl_robot(missionsDSL_Robot missionsdsl_robot) {
        this.missionsdsl_robot = missionsdsl_robot;
    }

}