





import java.util.List;
import java.util.ArrayList;

public class SBCS_PumpControler  {

    private boolean circulating;
    private boolean ready;





    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_Pump sbcs_pump;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_Pump sbcs_pump;




    private SBCS_Snapshot sbcs_snapshot;


    public SBCS_PumpControler(
        boolean circulating,        boolean ready    ) {
        this.circulating = circulating;
        this.ready = ready;
    }


    public boolean getCirculating() {
        return circulating;
    }

    public void setCirculating(boolean circulating) {
        this.circulating = circulating;
    }
    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }

    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_Pump getSbcs_pump() {
        return sbcs_pump;
    }

    public void setSbcs_pump(SBCS_Pump sbcs_pump) {
        this.sbcs_pump = sbcs_pump;
    }
    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }
    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }
    public SBCS_Pump getSbcs_pump() {
        return sbcs_pump;
    }

    public void setSbcs_pump(SBCS_Pump sbcs_pump) {
        this.sbcs_pump = sbcs_pump;
    }
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }

}