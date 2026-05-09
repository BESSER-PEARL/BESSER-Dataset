





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_RobotConfiguration  {

    private String robotIPAddress;
    private String robotSystemID;
    private int robotActivate;
    private String robotID;





    private MachineLibrary_RobotVarToBusyCodes machinelibrary_robotvartobusycodes;




    private MachineLibrary_RobotToWinccs machinelibrary_robottowinccs;




    private MachineLibrary_RobotVarToErrorbits machinelibrary_robotvartoerrorbits;




    private MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration;




    private MachineLibrary_RobotConfSendOrders machinelibrary_robotconfsendorders;




    private MachineLibrary_RobotWarningONDelete machinelibrary_robotwarningondelete;




    private MachineLibrary_RobotWinCCToRobots machinelibrary_robotwincctorobots;


    public MachineLibrary_RobotConfiguration(
        String robotIPAddress,        String robotSystemID,        int robotActivate,        String robotID    ) {
        this.robotIPAddress = robotIPAddress;
        this.robotSystemID = robotSystemID;
        this.robotActivate = robotActivate;
        this.robotID = robotID;
    }


    public String getRobotipaddress() {
        return robotIPAddress;
    }

    public void setRobotipaddress(String robotIPAddress) {
        this.robotIPAddress = robotIPAddress;
    }
    public String getRobotsystemid() {
        return robotSystemID;
    }

    public void setRobotsystemid(String robotSystemID) {
        this.robotSystemID = robotSystemID;
    }
    public int getRobotactivate() {
        return robotActivate;
    }

    public void setRobotactivate(int robotActivate) {
        this.robotActivate = robotActivate;
    }
    public String getRobotid() {
        return robotID;
    }

    public void setRobotid(String robotID) {
        this.robotID = robotID;
    }

    public MachineLibrary_RobotVarToBusyCodes getMachinelibrary_robotvartobusycodes() {
        return machinelibrary_robotvartobusycodes;
    }

    public void setMachinelibrary_robotvartobusycodes(MachineLibrary_RobotVarToBusyCodes machinelibrary_robotvartobusycodes) {
        this.machinelibrary_robotvartobusycodes = machinelibrary_robotvartobusycodes;
    }
    public MachineLibrary_RobotToWinccs getMachinelibrary_robottowinccs() {
        return machinelibrary_robottowinccs;
    }

    public void setMachinelibrary_robottowinccs(MachineLibrary_RobotToWinccs machinelibrary_robottowinccs) {
        this.machinelibrary_robottowinccs = machinelibrary_robottowinccs;
    }
    public MachineLibrary_RobotVarToErrorbits getMachinelibrary_robotvartoerrorbits() {
        return machinelibrary_robotvartoerrorbits;
    }

    public void setMachinelibrary_robotvartoerrorbits(MachineLibrary_RobotVarToErrorbits machinelibrary_robotvartoerrorbits) {
        this.machinelibrary_robotvartoerrorbits = machinelibrary_robotvartoerrorbits;
    }
    public MachineLibrary_NodeSpecialConfiguration getMachinelibrary_nodespecialconfiguration() {
        return machinelibrary_nodespecialconfiguration;
    }

    public void setMachinelibrary_nodespecialconfiguration(MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration) {
        this.machinelibrary_nodespecialconfiguration = machinelibrary_nodespecialconfiguration;
    }
    public MachineLibrary_RobotConfSendOrders getMachinelibrary_robotconfsendorders() {
        return machinelibrary_robotconfsendorders;
    }

    public void setMachinelibrary_robotconfsendorders(MachineLibrary_RobotConfSendOrders machinelibrary_robotconfsendorders) {
        this.machinelibrary_robotconfsendorders = machinelibrary_robotconfsendorders;
    }
    public MachineLibrary_RobotWarningONDelete getMachinelibrary_robotwarningondelete() {
        return machinelibrary_robotwarningondelete;
    }

    public void setMachinelibrary_robotwarningondelete(MachineLibrary_RobotWarningONDelete machinelibrary_robotwarningondelete) {
        this.machinelibrary_robotwarningondelete = machinelibrary_robotwarningondelete;
    }
    public MachineLibrary_RobotWinCCToRobots getMachinelibrary_robotwincctorobots() {
        return machinelibrary_robotwincctorobots;
    }

    public void setMachinelibrary_robotwincctorobots(MachineLibrary_RobotWinCCToRobots machinelibrary_robotwincctorobots) {
        this.machinelibrary_robotwincctorobots = machinelibrary_robotwincctorobots;
    }

}