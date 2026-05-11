





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaCommHost extends GRM_CommunicationMedia, GRM_Scheduler {






    private List<NFP_Real> nfp_reals;


    public MARTE_GQAM_GaCommHost(
    ) {
        super(
        );
        this.nfp_reals = new ArrayList<>();
    }

    public MARTE_GQAM_GaCommHost(
        ArrayList<NFP_Real> nfp_reals    ) {
        this.nfp_reals = nfp_reals;
    }


    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }

}