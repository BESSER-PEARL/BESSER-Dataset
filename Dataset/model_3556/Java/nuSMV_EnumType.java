





import java.util.List;
import java.util.ArrayList;

public class nuSMV_EnumType extends SimpleType {






    private List<nuSMV_Val> nusmv_vals;


    public nuSMV_EnumType(
    ) {
        super(
        );
        this.nusmv_vals = new ArrayList<>();
    }

    public nuSMV_EnumType(
        ArrayList<nuSMV_Val> nusmv_vals    ) {
        this.nusmv_vals = nusmv_vals;
    }


    public List<nuSMV_Val> getNusmv_vals() {
        return nusmv_vals;
    }

    public void addNusmv_val(Nusmv_val nusmv_val) {
        this.nusmv_vals.add(nusmv_val);
    }

}