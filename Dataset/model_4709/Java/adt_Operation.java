





import java.util.List;
import java.util.ArrayList;

public class adt_Operation  {

    private String name;





    private adt_Signature adt_signature;




    private adt_Signature adt_signature;




    private List<adt_ASort> adt_asorts;




    private adt_Signature adt_signature;




    private adt_ASort adt_asort;


    public adt_Operation(
        String name    ) {
        this.name = name;
        this.adt_asorts = new ArrayList<>();
    }

    public adt_Operation(
        String name        ArrayList<adt_ASort> adt_asorts    ) {
        this.name = name;
        this.adt_asorts = adt_asorts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adt_Signature getAdt_signature() {
        return adt_signature;
    }

    public void setAdt_signature(adt_Signature adt_signature) {
        this.adt_signature = adt_signature;
    }
    public adt_Signature getAdt_signature() {
        return adt_signature;
    }

    public void setAdt_signature(adt_Signature adt_signature) {
        this.adt_signature = adt_signature;
    }
    public List<adt_ASort> getAdt_asorts() {
        return adt_asorts;
    }

    public void addAdt_asort(Adt_asort adt_asort) {
        this.adt_asorts.add(adt_asort);
    }
    public adt_Signature getAdt_signature() {
        return adt_signature;
    }

    public void setAdt_signature(adt_Signature adt_signature) {
        this.adt_signature = adt_signature;
    }
    public adt_ASort getAdt_asort() {
        return adt_asort;
    }

    public void setAdt_asort(adt_ASort adt_asort) {
        this.adt_asort = adt_asort;
    }

}