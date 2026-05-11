





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaLatencyObs extends GaTimedObs {






    private List<NFP_Duration> nfp_durations;




    private List<NFP_Real> nfp_reals;




    private List<NFP_Duration> nfp_durations;




    private List<UtilityType> utilitytypes;


    public MARTE_GQAM_GaLatencyObs(
    ) {
        super(
        );
        this.nfp_durations = new ArrayList<>();
        this.nfp_reals = new ArrayList<>();
        this.nfp_durations = new ArrayList<>();
        this.utilitytypes = new ArrayList<>();
    }

    public MARTE_GQAM_GaLatencyObs(
        ArrayList<NFP_Duration> nfp_durations,        ArrayList<NFP_Real> nfp_reals,        ArrayList<NFP_Duration> nfp_durations,        ArrayList<UtilityType> utilitytypes    ) {
        this.nfp_durations = nfp_durations;
        this.nfp_reals = nfp_reals;
        this.nfp_durations = nfp_durations;
        this.utilitytypes = utilitytypes;
    }


    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }
    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<UtilityType> getUtilitytypes() {
        return utilitytypes;
    }

    public void addUtilitytype(Utilitytype utilitytype) {
        this.utilitytypes.add(utilitytype);
    }

}