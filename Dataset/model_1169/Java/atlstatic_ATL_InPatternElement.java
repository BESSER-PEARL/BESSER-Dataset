





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_InPatternElement extends PatternElement {






    private OutPatternElement outpatternelement;




    private List<OclModel> oclmodels;


    public atlstatic_ATL_InPatternElement(
    ) {
        super(
        );
        this.oclmodels = new ArrayList<>();
    }

    public atlstatic_ATL_InPatternElement(
        ArrayList<OclModel> oclmodels    ) {
        this.oclmodels = oclmodels;
    }


    public OutPatternElement getOutpatternelement() {
        return outpatternelement;
    }

    public void setOutpatternelement(OutPatternElement outpatternelement) {
        this.outpatternelement = outpatternelement;
    }
    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }

}