





import java.util.List;
import java.util.ArrayList;

public class SBCS_ControlProgram  {

    private String mode;





    private SBCS_SteamBoiler sbcs_steamboiler;




    private SBCS_ControlProgram_Start sbcs_controlprogram_start;


    public SBCS_ControlProgram(
        String mode    ) {
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public SBCS_SteamBoiler getSbcs_steamboiler() {
        return sbcs_steamboiler;
    }

    public void setSbcs_steamboiler(SBCS_SteamBoiler sbcs_steamboiler) {
        this.sbcs_steamboiler = sbcs_steamboiler;
    }
    public SBCS_ControlProgram_Start getSbcs_controlprogram_start() {
        return sbcs_controlprogram_start;
    }

    public void setSbcs_controlprogram_start(SBCS_ControlProgram_Start sbcs_controlprogram_start) {
        this.sbcs_controlprogram_start = sbcs_controlprogram_start;
    }

}