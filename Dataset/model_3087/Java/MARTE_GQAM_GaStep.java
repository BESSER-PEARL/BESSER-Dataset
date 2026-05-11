





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaStep extends GaScenario {






    private NFP_Duration nfp_duration;




    private NFP_Duration nfp_duration;




    private NFP_Real nfp_real;




    private List<GQAM_GaRequestedService> gqam_garequestedservices;




    private GQAM_GaExecHost gqam_gaexechost;




    private List<NFP_Real> nfp_reals;




    private NFP_Integer nfp_integer;




    private GRM_SchedulableResource grm_schedulableresource;




    private NFP_Real nfp_real;




    private GQAM_GaScenario gqam_gascenario;


    public MARTE_GQAM_GaStep(
    ) {
        super(
        );
        this.gqam_garequestedservices = new ArrayList<>();
        this.nfp_reals = new ArrayList<>();
    }

    public MARTE_GQAM_GaStep(
        ArrayList<GQAM_GaRequestedService> gqam_garequestedservices,        ArrayList<NFP_Real> nfp_reals    ) {
        this.gqam_garequestedservices = gqam_garequestedservices;
        this.nfp_reals = nfp_reals;
    }


    public NFP_Duration getNfp_duration() {
        return nfp_duration;
    }

    public void setNfp_duration(NFP_Duration nfp_duration) {
        this.nfp_duration = nfp_duration;
    }
    public NFP_Duration getNfp_duration() {
        return nfp_duration;
    }

    public void setNfp_duration(NFP_Duration nfp_duration) {
        this.nfp_duration = nfp_duration;
    }
    public NFP_Real getNfp_real() {
        return nfp_real;
    }

    public void setNfp_real(NFP_Real nfp_real) {
        this.nfp_real = nfp_real;
    }
    public List<GQAM_GaRequestedService> getGqam_garequestedservices() {
        return gqam_garequestedservices;
    }

    public void addGqam_garequestedservice(Gqam_garequestedservice gqam_garequestedservice) {
        this.gqam_garequestedservices.add(gqam_garequestedservice);
    }
    public GQAM_GaExecHost getGqam_gaexechost() {
        return gqam_gaexechost;
    }

    public void setGqam_gaexechost(GQAM_GaExecHost gqam_gaexechost) {
        this.gqam_gaexechost = gqam_gaexechost;
    }
    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }
    public NFP_Integer getNfp_integer() {
        return nfp_integer;
    }

    public void setNfp_integer(NFP_Integer nfp_integer) {
        this.nfp_integer = nfp_integer;
    }
    public GRM_SchedulableResource getGrm_schedulableresource() {
        return grm_schedulableresource;
    }

    public void setGrm_schedulableresource(GRM_SchedulableResource grm_schedulableresource) {
        this.grm_schedulableresource = grm_schedulableresource;
    }
    public NFP_Real getNfp_real() {
        return nfp_real;
    }

    public void setNfp_real(NFP_Real nfp_real) {
        this.nfp_real = nfp_real;
    }
    public GQAM_GaScenario getGqam_gascenario() {
        return gqam_gascenario;
    }

    public void setGqam_gascenario(GQAM_GaScenario gqam_gascenario) {
        this.gqam_gascenario = gqam_gascenario;
    }

}