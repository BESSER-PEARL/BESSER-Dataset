





import java.util.List;
import java.util.ArrayList;

public class eTJ_AccountShare  {

    private float share;





    private eTJ_ChargeSet etj_chargeset;




    private eTJ_Account etj_account;


    public eTJ_AccountShare(
        float share    ) {
        this.share = share;
    }


    public float getShare() {
        return share;
    }

    public void setShare(float share) {
        this.share = share;
    }

    public eTJ_ChargeSet getEtj_chargeset() {
        return etj_chargeset;
    }

    public void setEtj_chargeset(eTJ_ChargeSet etj_chargeset) {
        this.etj_chargeset = etj_chargeset;
    }
    public eTJ_Account getEtj_account() {
        return etj_account;
    }

    public void setEtj_account(eTJ_Account etj_account) {
        this.etj_account = etj_account;
    }

}