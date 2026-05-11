





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Angle extends Amount {

    private String angleUnit;





    private RobotProjectModel_Turn robotprojectmodel_turn;


    public RobotProjectModel_Angle(
        String angleUnit    ) {
        super(
        );
        this.angleUnit = angleUnit;
    }


    public String getAngleunit() {
        return angleUnit;
    }

    public void setAngleunit(String angleUnit) {
        this.angleUnit = angleUnit;
    }

    public RobotProjectModel_Turn getRobotprojectmodel_turn() {
        return robotprojectmodel_turn;
    }

    public void setRobotprojectmodel_turn(RobotProjectModel_Turn robotprojectmodel_turn) {
        this.robotprojectmodel_turn = robotprojectmodel_turn;
    }

}