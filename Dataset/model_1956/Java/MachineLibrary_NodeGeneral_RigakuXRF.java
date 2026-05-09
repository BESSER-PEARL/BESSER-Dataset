





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral_RigakuXRF  {

    private int timeoutResponce;
    private int timerToSendStatus;
    private int timeout;
    private int bDoNotshiftAtExit;





    private MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial;


    public MachineLibrary_NodeGeneral_RigakuXRF(
        int timeoutResponce,        int timerToSendStatus,        int timeout,        int bDoNotshiftAtExit    ) {
        this.timeoutResponce = timeoutResponce;
        this.timerToSendStatus = timerToSendStatus;
        this.timeout = timeout;
        this.bDoNotshiftAtExit = bDoNotshiftAtExit;
    }


    public int getTimeoutresponce() {
        return timeoutResponce;
    }

    public void setTimeoutresponce(int timeoutResponce) {
        this.timeoutResponce = timeoutResponce;
    }
    public int getTimertosendstatus() {
        return timerToSendStatus;
    }

    public void setTimertosendstatus(int timerToSendStatus) {
        this.timerToSendStatus = timerToSendStatus;
    }
    public int getTimeout() {
        return timeout;
    }

    public void setTimeout(int timeout) {
        this.timeout = timeout;
    }
    public int getBdonotshiftatexit() {
        return bDoNotshiftAtExit;
    }

    public void setBdonotshiftatexit(int bDoNotshiftAtExit) {
        this.bDoNotshiftAtExit = bDoNotshiftAtExit;
    }

    public MachineLibrary_NodeGeneralSpecial getMachinelibrary_nodegeneralspecial() {
        return machinelibrary_nodegeneralspecial;
    }

    public void setMachinelibrary_nodegeneralspecial(MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial) {
        this.machinelibrary_nodegeneralspecial = machinelibrary_nodegeneralspecial;
    }

}