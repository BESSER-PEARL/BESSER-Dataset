





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_RobotWarningONDelete  {

    private String robotExtraUnit_2;
    private int robotErrBitWhenConfirmationIsNeededFor_Robot;
    private String robotExtraPos_1;
    private int robotErrBitWhenConfirmationIsNeededFor_PM;



    public MachineLibrary_RobotWarningONDelete(
        String robotExtraUnit_2,        int robotErrBitWhenConfirmationIsNeededFor_Robot,        String robotExtraPos_1,        int robotErrBitWhenConfirmationIsNeededFor_PM    ) {
        this.robotExtraUnit_2 = robotExtraUnit_2;
        this.robotErrBitWhenConfirmationIsNeededFor_Robot = robotErrBitWhenConfirmationIsNeededFor_Robot;
        this.robotExtraPos_1 = robotExtraPos_1;
        this.robotErrBitWhenConfirmationIsNeededFor_PM = robotErrBitWhenConfirmationIsNeededFor_PM;
    }


    public String getRobotextraunit_2() {
        return robotExtraUnit_2;
    }

    public void setRobotextraunit_2(String robotExtraUnit_2) {
        this.robotExtraUnit_2 = robotExtraUnit_2;
    }
    public int getRoboterrbitwhenconfirmationisneededfor_robot() {
        return robotErrBitWhenConfirmationIsNeededFor_Robot;
    }

    public void setRoboterrbitwhenconfirmationisneededfor_robot(int robotErrBitWhenConfirmationIsNeededFor_Robot) {
        this.robotErrBitWhenConfirmationIsNeededFor_Robot = robotErrBitWhenConfirmationIsNeededFor_Robot;
    }
    public String getRobotextrapos_1() {
        return robotExtraPos_1;
    }

    public void setRobotextrapos_1(String robotExtraPos_1) {
        this.robotExtraPos_1 = robotExtraPos_1;
    }
    public int getRoboterrbitwhenconfirmationisneededfor_pm() {
        return robotErrBitWhenConfirmationIsNeededFor_PM;
    }

    public void setRoboterrbitwhenconfirmationisneededfor_pm(int robotErrBitWhenConfirmationIsNeededFor_PM) {
        this.robotErrBitWhenConfirmationIsNeededFor_PM = robotErrBitWhenConfirmationIsNeededFor_PM;
    }


}