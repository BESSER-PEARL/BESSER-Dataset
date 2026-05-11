





import java.util.List;
import java.util.ArrayList;

public class MARTE_PAM_PaRunTInstance  {

    private String unbddPool;





    private NFP_Integer nfp_integer;




    private GRM_SchedulableResource grm_schedulableresource;




    private GQAM_GaExecHost gqam_gaexechost;




    private NFP_Frequency nfp_frequency;




    private NFP_Real nfp_real;


    public MARTE_PAM_PaRunTInstance(
        String unbddPool    ) {
        this.unbddPool = unbddPool;
    }


    public String getUnbddpool() {
        return unbddPool;
    }

    public void setUnbddpool(String unbddPool) {
        this.unbddPool = unbddPool;
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
    public GQAM_GaExecHost getGqam_gaexechost() {
        return gqam_gaexechost;
    }

    public void setGqam_gaexechost(GQAM_GaExecHost gqam_gaexechost) {
        this.gqam_gaexechost = gqam_gaexechost;
    }
    public NFP_Frequency getNfp_frequency() {
        return nfp_frequency;
    }

    public void setNfp_frequency(NFP_Frequency nfp_frequency) {
        this.nfp_frequency = nfp_frequency;
    }
    public NFP_Real getNfp_real() {
        return nfp_real;
    }

    public void setNfp_real(NFP_Real nfp_real) {
        this.nfp_real = nfp_real;
    }

}