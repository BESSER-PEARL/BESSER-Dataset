





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaCommChannel extends SchedulableResource {






    private List<NFP_Real> nfp_reals;




    private NFP_DataSize nfp_datasize;


    public MARTE_GQAM_GaCommChannel(
    ) {
        super(
        );
        this.nfp_reals = new ArrayList<>();
    }

    public MARTE_GQAM_GaCommChannel(
        ArrayList<NFP_Real> nfp_reals    ) {
        this.nfp_reals = nfp_reals;
    }


    public List<NFP_Real> getNfp_reals() {
        return nfp_reals;
    }

    public void addNfp_real(Nfp_real nfp_real) {
        this.nfp_reals.add(nfp_real);
    }
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }

}