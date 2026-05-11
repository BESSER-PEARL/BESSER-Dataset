





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Distance extends Amount {

    private String distanceUnit;





    private RobotProjectModel_MoveStraight robotprojectmodel_movestraight;


    public RobotProjectModel_Distance(
        String distanceUnit    ) {
        super(
        );
        this.distanceUnit = distanceUnit;
    }


    public String getDistanceunit() {
        return distanceUnit;
    }

    public void setDistanceunit(String distanceUnit) {
        this.distanceUnit = distanceUnit;
    }

    public RobotProjectModel_MoveStraight getRobotprojectmodel_movestraight() {
        return robotprojectmodel_movestraight;
    }

    public void setRobotprojectmodel_movestraight(RobotProjectModel_MoveStraight robotprojectmodel_movestraight) {
        this.robotprojectmodel_movestraight = robotprojectmodel_movestraight;
    }

}