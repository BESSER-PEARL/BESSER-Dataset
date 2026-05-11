





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaSchedObs extends GaTimedObs {






    private List<NFP_Duration> nfp_durations;




    private List<NFP_Integer> nfp_integers;




    private List<NFP_Integer> nfp_integers;


    public MARTE_SAM_SaSchedObs(
    ) {
        super(
        );
        this.nfp_durations = new ArrayList<>();
        this.nfp_integers = new ArrayList<>();
        this.nfp_integers = new ArrayList<>();
    }

    public MARTE_SAM_SaSchedObs(
        ArrayList<NFP_Duration> nfp_durations,        ArrayList<NFP_Integer> nfp_integers,        ArrayList<NFP_Integer> nfp_integers    ) {
        this.nfp_durations = nfp_durations;
        this.nfp_integers = nfp_integers;
        this.nfp_integers = nfp_integers;
    }


    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<NFP_Integer> getNfp_integers() {
        return nfp_integers;
    }

    public void addNfp_integer(Nfp_integer nfp_integer) {
        this.nfp_integers.add(nfp_integer);
    }
    public List<NFP_Integer> getNfp_integers() {
        return nfp_integers;
    }

    public void addNfp_integer(Nfp_integer nfp_integer) {
        this.nfp_integers.add(nfp_integer);
    }

}