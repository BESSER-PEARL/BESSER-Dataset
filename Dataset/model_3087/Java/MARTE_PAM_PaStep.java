





import java.util.List;
import java.util.ArrayList;

public class MARTE_PAM_PaStep extends GaStep {

    private String extOpDemand;





    private List<NFP_Real> nfp_reals;




    private List<GQAM_GaScenario> gqam_gascenarios;




    private List<NFP_Real> nfp_reals;


    public MARTE_PAM_PaStep(
        String extOpDemand    ) {
        super(
        );
        this.extOpDemand = extOpDemand;
        this.nfp_reals = new ArrayList<>();
        this.gqam_gascenarios = new ArrayList<>();
        this.nfp_reals = new ArrayList<>();
    }

    public MARTE_PAM_PaStep(
        String extOpDemand        ArrayList<NFP_Real> nfp_reals,        ArrayList<GQAM_GaScenario> gqam_gascenarios,        ArrayList<NFP_Real> nfp_reals    ) {
        this.extOpDemand = extOpDemand;
        this.nfp_reals = nfp_reals;
        this.gqam_gascenarios = gqam_gascenarios;
        this.nfp_reals = nfp_reals;
    }

    public String getExtopdemand() {
        return extOpDemand;
    }

    public void setExtopdemand(String extOpDemand) {
        this.extOpDemand = extOpDemand;
    }

    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }
    public List<GQAM_GaScenario> getGqam_gascenarios() {
        return gqam_gascenarios;
    }

    public void addGqam_gascenario(Gqam_gascenario gqam_gascenario) {
        this.gqam_gascenarios.add(gqam_gascenario);
    }
    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }

}