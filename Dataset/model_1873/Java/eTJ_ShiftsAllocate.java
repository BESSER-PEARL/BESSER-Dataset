





import java.util.List;
import java.util.ArrayList;

public class eTJ_ShiftsAllocate extends AllocateResourceAttribute {






    private eTJ_Shift etj_shift;




    private List<eTJ_Interval3> etj_interval3s;


    public eTJ_ShiftsAllocate(
    ) {
        super(
        );
        this.etj_interval3s = new ArrayList<>();
    }

    public eTJ_ShiftsAllocate(
        ArrayList<eTJ_Interval3> etj_interval3s    ) {
        this.etj_interval3s = etj_interval3s;
    }


    public eTJ_Shift getEtj_shift() {
        return etj_shift;
    }

    public void setEtj_shift(eTJ_Shift etj_shift) {
        this.etj_shift = etj_shift;
    }
    public List<eTJ_Interval3> getEtj_interval3s() {
        return etj_interval3s;
    }

    public void addEtj_interval3(Etj_interval3 etj_interval3) {
        this.etj_interval3s.add(etj_interval3);
    }

}