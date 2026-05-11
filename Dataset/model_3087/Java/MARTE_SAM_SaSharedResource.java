





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaSharedResource extends MutualExclusionResource {






    private List<NFP_Duration> nfp_durations;




    private List<NFP_Duration> nfp_durations;




    private NFP_Integer nfp_integer;


    public MARTE_SAM_SaSharedResource(
    ) {
        super(
        );
        this.nfp_durations = new ArrayList<>();
        this.nfp_durations = new ArrayList<>();
    }

    public MARTE_SAM_SaSharedResource(
        ArrayList<NFP_Duration> nfp_durations,        ArrayList<NFP_Duration> nfp_durations    ) {
        this.nfp_durations = nfp_durations;
        this.nfp_durations = nfp_durations;
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
    public NFP_Integer getNfp_integer() {
        return nfp_integer;
    }

    public void setNfp_integer(NFP_Integer nfp_integer) {
        this.nfp_integer = nfp_integer;
    }

}