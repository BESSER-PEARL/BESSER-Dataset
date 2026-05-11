





import java.util.List;
import java.util.ArrayList;

public class adt_Signature  {

    private String ops;





    private adt_ADT adt_adt;




    private List<adt_ASort> adt_asorts;


    public adt_Signature(
        String ops    ) {
        this.ops = ops;
        this.adt_asorts = new ArrayList<>();
    }

    public adt_Signature(
        String ops        ArrayList<adt_ASort> adt_asorts    ) {
        this.ops = ops;
        this.adt_asorts = adt_asorts;
    }

    public String getOps() {
        return ops;
    }

    public void setOps(String ops) {
        this.ops = ops;
    }

    public adt_ADT getAdt_adt() {
        return adt_adt;
    }

    public void setAdt_adt(adt_ADT adt_adt) {
        this.adt_adt = adt_adt;
    }
    public List<adt_ASort> getAdt_asorts() {
        return adt_asorts;
    }

    public void addAdt_asort(Adt_asort adt_asort) {
        this.adt_asorts.add(adt_asort);
    }

}