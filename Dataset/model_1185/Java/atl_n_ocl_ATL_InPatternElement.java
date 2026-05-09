





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_ATL_InPatternElement extends PatternElement {






    private List<OclModel> oclmodels;


    public atl_n_ocl_ATL_InPatternElement(
    ) {
        super(
        );
        this.oclmodels = new ArrayList<>();
    }

    public atl_n_ocl_ATL_InPatternElement(
        ArrayList<OclModel> oclmodels    ) {
        this.oclmodels = oclmodels;
    }


    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }

}