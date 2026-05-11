





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaWorkloadBehavior  {






    private List<GQAM_GaScenario> gqam_gascenarios;




    private GQAM_MARTE_NamedElement gqam_marte_namedelement;




    private List<GQAM_GaWorkloadEvent> gqam_gaworkloadevents;


    public MARTE_GQAM_GaWorkloadBehavior(
    ) {
        this.gqam_gascenarios = new ArrayList<>();
        this.gqam_gaworkloadevents = new ArrayList<>();
    }

    public MARTE_GQAM_GaWorkloadBehavior(
        ArrayList<GQAM_GaScenario> gqam_gascenarios,        ArrayList<GQAM_GaWorkloadEvent> gqam_gaworkloadevents    ) {
        this.gqam_gascenarios = gqam_gascenarios;
        this.gqam_gaworkloadevents = gqam_gaworkloadevents;
    }


    public List<GQAM_GaScenario> getGqam_gascenarios() {
        return gqam_gascenarios;
    }

    public void addGqam_gascenario(Gqam_gascenario gqam_gascenario) {
        this.gqam_gascenarios.add(gqam_gascenario);
    }
    public GQAM_MARTE_NamedElement getGqam_marte_namedelement() {
        return gqam_marte_namedelement;
    }

    public void setGqam_marte_namedelement(GQAM_MARTE_NamedElement gqam_marte_namedelement) {
        this.gqam_marte_namedelement = gqam_marte_namedelement;
    }
    public List<GQAM_GaWorkloadEvent> getGqam_gaworkloadevents() {
        return gqam_gaworkloadevents;
    }

    public void addGqam_gaworkloadevent(Gqam_gaworkloadevent gqam_gaworkloadevent) {
        this.gqam_gaworkloadevents.add(gqam_gaworkloadevent);
    }

}