





import java.util.List;
import java.util.ArrayList;

public class SBCS_SteamBoiler  {

    private String valveOpen;
    private float maximalNormal;
    private float capacity;





    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;




    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;


    public SBCS_SteamBoiler(
        String valveOpen,        float maximalNormal,        float capacity    ) {
        this.valveOpen = valveOpen;
        this.maximalNormal = maximalNormal;
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
    public float getCapacity() {
        return capacity;
    }

    public void setCapacity(float capacity) {
        this.capacity = capacity;
    }

    public SBCS_SteamBoiler_OpenValve getSbcs_steamboiler_openvalve() {
        return sbcs_steamboiler_openvalve;
    }

    public void setSbcs_steamboiler_openvalve(SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve) {
        this.sbcs_steamboiler_openvalve = sbcs_steamboiler_openvalve;
    }
    public SBCS_SteamBoiler_OpenValve getSbcs_steamboiler_openvalve() {
        return sbcs_steamboiler_openvalve;
    }

    public void setSbcs_steamboiler_openvalve(SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve) {
        this.sbcs_steamboiler_openvalve = sbcs_steamboiler_openvalve;
    }

}