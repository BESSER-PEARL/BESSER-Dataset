





import java.util.List;
import java.util.ArrayList;

public class SBCS_SteamBoiler  {

    private String valveOpen;





    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_SteamBoiler_OpenValve sbcs_steamboiler_openvalve;


    public SBCS_SteamBoiler(
        String valveOpen    ) {
        this.valveOpen = valveOpen;
    }


    public String getValveopen() {
        return valveOpen;
    }

    public void setValveopen(String valveOpen) {
        this.valveOpen = valveOpen;
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