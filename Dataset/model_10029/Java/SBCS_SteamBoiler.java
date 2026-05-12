





import java.util.List;
import java.util.ArrayList;

public class SBCS_SteamBoiler  {

    private float minimalNormal;
    private float capacity;
    private String valveOpen;
    private float maximalNormal;





    private SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice;




    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;


    public SBCS_SteamBoiler(
        float minimalNormal,        float capacity,        String valveOpen,        float maximalNormal    ) {
        this.minimalNormal = minimalNormal;
        this.capacity = capacity;
        this.valveOpen = valveOpen;
        this.maximalNormal = maximalNormal;
    }


    public float getMinimalnormal() {
        return minimalNormal;
    }

    public void setMinimalnormal(float minimalNormal) {
        this.minimalNormal = minimalNormal;
    }
    public float getCapacity() {
        return capacity;
    }

    public void setCapacity(float capacity) {
        this.capacity = capacity;
    }
    public String getValveopen() {
        return valveOpen;
    }

    public void setValveopen(String valveOpen) {
        this.valveOpen = valveOpen;
    }
    public float getMaximalnormal() {
        return maximalNormal;
    }

    public void setMaximalnormal(float maximalNormal) {
        this.maximalNormal = maximalNormal;
    }

    public SBCS_WaterLevelMeasurementDevice getSbcs_waterlevelmeasurementdevice() {
        return sbcs_waterlevelmeasurementdevice;
    }

    public void setSbcs_waterlevelmeasurementdevice(SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice) {
        this.sbcs_waterlevelmeasurementdevice = sbcs_waterlevelmeasurementdevice;
    }
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_WaterLevelMeasurementDevice getSbcs_waterlevelmeasurementdevice() {
        return sbcs_waterlevelmeasurementdevice;
    }

    public void setSbcs_waterlevelmeasurementdevice(SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice) {
        this.sbcs_waterlevelmeasurementdevice = sbcs_waterlevelmeasurementdevice;
    }
    public SBCS_SteamBoiler_OpenValve getSbcs_steamboiler_openvalve() {
        return sbcs_steamboiler_openvalve;
    }

    public void setSbcs_steamboiler_openvalve(SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve) {
        this.sbcs_steamboiler_openvalve = sbcs_steamboiler_openvalve;
    }
    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }
    public SBCS_SteamBoiler_OpenValve getSbcs_steamboiler_openvalve() {
        return sbcs_steamboiler_openvalve;
    }

    public void setSbcs_steamboiler_openvalve(SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve) {
        this.sbcs_steamboiler_openvalve = sbcs_steamboiler_openvalve;
    }

}