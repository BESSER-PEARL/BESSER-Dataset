





import java.util.List;
import java.util.ArrayList;

public class eTJ_WorkingHours extends ResourceAttribute, ProjectAttribute {

    private boolean off;





    private eTJ_Shift etj_shift;


    public eTJ_WorkingHours(
        boolean off    ) {
        super(
        );
        this.off = off;
    }


    public boolean getOff() {
        return off;
    }

    public void setOff(boolean off) {
        this.off = off;
    }

    public eTJ_Shift getEtj_shift() {
        return etj_shift;
    }

    public void setEtj_shift(eTJ_Shift etj_shift) {
        this.etj_shift = etj_shift;
    }

}