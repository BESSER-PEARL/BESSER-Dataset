





import java.util.List;
import java.util.ArrayList;

public class xpdl1_TimeEstimationType  {

    private String workingTime;
    private String duration;
    private String waitingTime;





    private xpdl1_SimulationInformationType xpdl1_simulationinformationtype;




    private xpdl1_ProcessHeaderType xpdl1_processheadertype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_TimeEstimationType(
        String workingTime,        String duration,        String waitingTime    ) {
        this.workingTime = workingTime;
        this.duration = duration;
        this.waitingTime = waitingTime;
    }


    public String getWorkingtime() {
        return workingTime;
    }

    public void setWorkingtime(String workingTime) {
        this.workingTime = workingTime;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getWaitingtime() {
        return waitingTime;
    }

    public void setWaitingtime(String waitingTime) {
        this.waitingTime = waitingTime;
    }

    public xpdl1_SimulationInformationType getXpdl1_simulationinformationtype() {
        return xpdl1_simulationinformationtype;
    }

    public void setXpdl1_simulationinformationtype(xpdl1_SimulationInformationType xpdl1_simulationinformationtype) {
        this.xpdl1_simulationinformationtype = xpdl1_simulationinformationtype;
    }
    public xpdl1_ProcessHeaderType getXpdl1_processheadertype() {
        return xpdl1_processheadertype;
    }

    public void setXpdl1_processheadertype(xpdl1_ProcessHeaderType xpdl1_processheadertype) {
        this.xpdl1_processheadertype = xpdl1_processheadertype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}