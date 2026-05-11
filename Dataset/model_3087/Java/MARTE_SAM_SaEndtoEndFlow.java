





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaEndtoEndFlow  {






    private NFP_Real nfp_real;




    private List<NFP_Duration> nfp_durations;




    private List<NFP_Duration> nfp_durations;




    private List<GQAM_GaTimedObs> gqam_gatimedobss;


    public MARTE_SAM_SaEndtoEndFlow(
    ) {
        this.nfp_durations = new ArrayList<>();
        this.nfp_durations = new ArrayList<>();
        this.gqam_gatimedobss = new ArrayList<>();
    }

    public MARTE_SAM_SaEndtoEndFlow(
        ArrayList<NFP_Duration> nfp_durations,        ArrayList<NFP_Duration> nfp_durations,        ArrayList<GQAM_GaTimedObs> gqam_gatimedobss    ) {
        this.nfp_durations = nfp_durations;
        this.nfp_durations = nfp_durations;
        this.gqam_gatimedobss = gqam_gatimedobss;
    }


    public NFP_Real getNfp_real() {
        return nfp_real;
    }

    public void setNfp_real(NFP_Real nfp_real) {
        this.nfp_real = nfp_real;
    }
    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<GQAM_GaTimedObs> getGqam_gatimedobss() {
        return gqam_gatimedobss;
    }

    public void addGqam_gatimedobs(Gqam_gatimedobs gqam_gatimedobs) {
        this.gqam_gatimedobss.add(gqam_gatimedobs);
    }

}