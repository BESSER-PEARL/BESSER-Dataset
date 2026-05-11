





import java.util.List;
import java.util.ArrayList;

public class MARTE_PAM_PaStep extends GaStep {

    private String noSync;
    private String extOpCount;
    private String extOpDemand;
    private String behavCount;





    private List<GQAM_GaScenario> gqam_gascenarios;


    public MARTE_PAM_PaStep(
        String noSync,        String extOpCount,        String extOpDemand,        String behavCount    ) {
        super(
        );
        this.noSync = noSync;
        this.extOpCount = extOpCount;
        this.extOpDemand = extOpDemand;
        this.behavCount = behavCount;
        this.gqam_gascenarios = new ArrayList<>();
    }

    public MARTE_PAM_PaStep(
        String noSync,        String extOpCount,        String extOpDemand,        String behavCount        ArrayList<GQAM_GaScenario> gqam_gascenarios    ) {
        this.noSync = noSync;
        this.extOpCount = extOpCount;
        this.extOpDemand = extOpDemand;
        this.behavCount = behavCount;
        this.gqam_gascenarios = gqam_gascenarios;
    }

    public String getNosync() {
        return noSync;
    }

    public void setNosync(String noSync) {
        this.noSync = noSync;
    }
    public String getExtopcount() {
        return extOpCount;
    }

    public void setExtopcount(String extOpCount) {
        this.extOpCount = extOpCount;
    }
    public String getExtopdemand() {
        return extOpDemand;
    }

    public void setExtopdemand(String extOpDemand) {
        this.extOpDemand = extOpDemand;
    }
    public String getBehavcount() {
        return behavCount;
    }

    public void setBehavcount(String behavCount) {
        this.behavCount = behavCount;
    }

    public List<GQAM_GaScenario> getGqam_gascenarios() {
        return gqam_gascenarios;
    }

    public void addGqam_gascenario(Gqam_gascenario gqam_gascenario) {
        this.gqam_gascenarios.add(gqam_gascenario);
    }

}