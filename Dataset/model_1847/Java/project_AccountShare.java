





import java.util.List;
import java.util.ArrayList;

public class project_AccountShare  {

    private float share;





    private project_ChargeSet project_chargeset;


    public project_AccountShare(
        float share    ) {
        this.share = share;
    }


    public float getShare() {
        return share;
    }

    public void setShare(float share) {
        this.share = share;
    }

    public project_ChargeSet getProject_chargeset() {
        return project_chargeset;
    }

    public void setProject_chargeset(project_ChargeSet project_chargeset) {
        this.project_chargeset = project_chargeset;
    }

}