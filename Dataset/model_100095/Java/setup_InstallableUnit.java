





import java.util.List;
import java.util.ArrayList;

public class setup_InstallableUnit  {

    private String iD;
    private String versionRange;





    private setup_P2Task setup_p2task;


    public setup_InstallableUnit(
        String iD,        String versionRange    ) {
        this.iD = iD;
        this.versionRange = versionRange;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }

    public setup_P2Task getSetup_p2task() {
        return setup_p2task;
    }

    public void setSetup_p2task(setup_P2Task setup_p2task) {
        this.setup_p2task = setup_p2task;
    }

}