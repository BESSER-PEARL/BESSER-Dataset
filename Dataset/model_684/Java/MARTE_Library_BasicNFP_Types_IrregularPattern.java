





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_IrregularPattern extends AperiodicPattern {






    private NFP_Duration nfp_duration;




    private List<NFP_Duration> nfp_durations;


    public MARTE_Library_BasicNFP_Types_IrregularPattern(
    ) {
        super(
        );
        this.nfp_durations = new ArrayList<>();
    }

    public MARTE_Library_BasicNFP_Types_IrregularPattern(
        ArrayList<NFP_Duration> nfp_durations    ) {
        this.nfp_durations = nfp_durations;
    }


    public NFP_Duration getNfp_duration() {
        return nfp_duration;
    }

    public void setNfp_duration(NFP_Duration nfp_duration) {
        this.nfp_duration = nfp_duration;
    }
    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }

}