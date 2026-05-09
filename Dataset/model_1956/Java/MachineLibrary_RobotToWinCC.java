





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_RobotToWinCC  {

    private String robotToWinccType_X;
    private int robotToWinccSeq_X;
    private String robotToWinccFrom_X;
    private String robotToWinccTo_X;





    private MachineLibrary_RobotToWinccs machinelibrary_robottowinccs;


    public MachineLibrary_RobotToWinCC(
        String robotToWinccType_X,        int robotToWinccSeq_X,        String robotToWinccFrom_X,        String robotToWinccTo_X    ) {
        this.robotToWinccType_X = robotToWinccType_X;
        this.robotToWinccSeq_X = robotToWinccSeq_X;
        this.robotToWinccFrom_X = robotToWinccFrom_X;
        this.robotToWinccTo_X = robotToWinccTo_X;
    }


    public String getRobottowincctype_x() {
        return robotToWinccType_X;
    }

    public void setRobottowincctype_x(String robotToWinccType_X) {
        this.robotToWinccType_X = robotToWinccType_X;
    }
    public int getRobottowinccseq_x() {
        return robotToWinccSeq_X;
    }

    public void setRobottowinccseq_x(int robotToWinccSeq_X) {
        this.robotToWinccSeq_X = robotToWinccSeq_X;
    }
    public String getRobottowinccfrom_x() {
        return robotToWinccFrom_X;
    }

    public void setRobottowinccfrom_x(String robotToWinccFrom_X) {
        this.robotToWinccFrom_X = robotToWinccFrom_X;
    }
    public String getRobottowinccto_x() {
        return robotToWinccTo_X;
    }

    public void setRobottowinccto_x(String robotToWinccTo_X) {
        this.robotToWinccTo_X = robotToWinccTo_X;
    }

    public MachineLibrary_RobotToWinccs getMachinelibrary_robottowinccs() {
        return machinelibrary_robottowinccs;
    }

    public void setMachinelibrary_robottowinccs(MachineLibrary_RobotToWinccs machinelibrary_robottowinccs) {
        this.machinelibrary_robottowinccs = machinelibrary_robottowinccs;
    }

}