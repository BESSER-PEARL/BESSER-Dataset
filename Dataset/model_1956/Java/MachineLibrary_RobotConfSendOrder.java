





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_RobotConfSendOrder  {

    private int robotconfsendorderSeq_X;
    private String robotconfsendorderFrom_X;
    private String robotconfsendorderVar_X;
    private String robotconfsendorderType_X;





    private MachineLibrary_RobotConfSendOrders machinelibrary_robotconfsendorders;


    public MachineLibrary_RobotConfSendOrder(
        int robotconfsendorderSeq_X,        String robotconfsendorderFrom_X,        String robotconfsendorderVar_X,        String robotconfsendorderType_X    ) {
        this.robotconfsendorderSeq_X = robotconfsendorderSeq_X;
        this.robotconfsendorderFrom_X = robotconfsendorderFrom_X;
        this.robotconfsendorderVar_X = robotconfsendorderVar_X;
        this.robotconfsendorderType_X = robotconfsendorderType_X;
    }


    public int getRobotconfsendorderseq_x() {
        return robotconfsendorderSeq_X;
    }

    public void setRobotconfsendorderseq_x(int robotconfsendorderSeq_X) {
        this.robotconfsendorderSeq_X = robotconfsendorderSeq_X;
    }
    public String getRobotconfsendorderfrom_x() {
        return robotconfsendorderFrom_X;
    }

    public void setRobotconfsendorderfrom_x(String robotconfsendorderFrom_X) {
        this.robotconfsendorderFrom_X = robotconfsendorderFrom_X;
    }
    public String getRobotconfsendordervar_x() {
        return robotconfsendorderVar_X;
    }

    public void setRobotconfsendordervar_x(String robotconfsendorderVar_X) {
        this.robotconfsendorderVar_X = robotconfsendorderVar_X;
    }
    public String getRobotconfsendordertype_x() {
        return robotconfsendorderType_X;
    }

    public void setRobotconfsendordertype_x(String robotconfsendorderType_X) {
        this.robotconfsendorderType_X = robotconfsendorderType_X;
    }

    public MachineLibrary_RobotConfSendOrders getMachinelibrary_robotconfsendorders() {
        return machinelibrary_robotconfsendorders;
    }

    public void setMachinelibrary_robotconfsendorders(MachineLibrary_RobotConfSendOrders machinelibrary_robotconfsendorders) {
        this.machinelibrary_robotconfsendorders = machinelibrary_robotconfsendorders;
    }

}