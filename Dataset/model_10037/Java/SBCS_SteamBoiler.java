





import java.util.List;
import java.util.ArrayList;

public class SBCS_SteamBoiler  {

    private float capacity;
    private float maximumDecrease;
    private float maximumIncrease;
    private boolean ready;
    private float maximalLimit;
    private float maximalNormal;
    private String valveOpen;
    private float minimalNormal;
    private float minimalLimit;





    private SBCS_Pump sbcs_pump;




    private SBCS_Pump sbcs_pump;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_ControlProgram sbcs_controlprogram;


    public SBCS_SteamBoiler(
        float capacity,        float maximumDecrease,        float maximumIncrease,        boolean ready,        float maximalLimit,        float maximalNormal,        String valveOpen,        float minimalNormal,        float minimalLimit    ) {
        this.capacity = capacity;
        this.maximumDecrease = maximumDecrease;
        this.maximumIncrease = maximumIncrease;
        this.ready = ready;
        this.maximalLimit = maximalLimit;
        this.maximalNormal = maximalNormal;
        this.valveOpen = valveOpen;
        this.minimalNormal = minimalNormal;
        this.minimalLimit = minimalLimit;
    }


    public float getCapacity() {
        return capacity;
    }

    public void setCapacity(float capacity) {
        this.capacity = capacity;
    }
    public float getMaximumdecrease() {
        return maximumDecrease;
    }

    public void setMaximumdecrease(float maximumDecrease) {
        this.maximumDecrease = maximumDecrease;
    }
    public float getMaximumincrease() {
        return maximumIncrease;
    }

    public void setMaximumincrease(float maximumIncrease) {
        this.maximumIncrease = maximumIncrease;
    }
    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public float getMaximallimit() {
        return maximalLimit;
    }

    public void setMaximallimit(float maximalLimit) {
        this.maximalLimit = maximalLimit;
    }
    public float getMaximalnormal() {
        return maximalNormal;
    }

    public void setMaximalnormal(float maximalNormal) {
        this.maximalNormal = maximalNormal;
    }
    public String getValveopen() {
        return valveOpen;
    }

    public void setValveopen(String valveOpen) {
        this.valveOpen = valveOpen;
    }
    public float getMinimalnormal() {
        return minimalNormal;
    }

    public void setMinimalnormal(float minimalNormal) {
        this.minimalNormal = minimalNormal;
    }
    public float getMinimallimit() {
        return minimalLimit;
    }

    public void setMinimallimit(float minimalLimit) {
        this.minimalLimit = minimalLimit;
    }

    public SBCS_Pump getSbcs_pump() {
        return sbcs_pump;
    }

    public void setSbcs_pump(SBCS_Pump sbcs_pump) {
        this.sbcs_pump = sbcs_pump;
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
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }

}