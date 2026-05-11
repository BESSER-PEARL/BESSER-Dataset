





import java.util.List;
import java.util.ArrayList;

public class RobotProjectModel_Duration extends Amount {

    private String timeUnit;





    private RobotProjectModel_TimedInstruction robotprojectmodel_timedinstruction;


    public RobotProjectModel_Duration(
        String timeUnit    ) {
        super(
        );
        this.timeUnit = timeUnit;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }

    public RobotProjectModel_TimedInstruction getRobotprojectmodel_timedinstruction() {
        return robotprojectmodel_timedinstruction;
    }

    public void setRobotprojectmodel_timedinstruction(RobotProjectModel_TimedInstruction robotprojectmodel_timedinstruction) {
        this.robotprojectmodel_timedinstruction = robotprojectmodel_timedinstruction;
    }

}