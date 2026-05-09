





import java.util.List;
import java.util.ArrayList;

public class ATL_InPatternElement extends PatternElement {






    private OutPatternElement outpatternelement;




    private InPattern inpattern;




    private List<OclModel> oclmodels;


    public ATL_InPatternElement(
    ) {
        super(
        );
        this.oclmodels = new ArrayList<>();
    }

    public ATL_InPatternElement(
        ArrayList<OclModel> oclmodels    ) {
        this.oclmodels = oclmodels;
    }


    public OutPatternElement getOutpatternelement() {
        return outpatternelement;
    }

    public void setOutpatternelement(OutPatternElement outpatternelement) {
        this.outpatternelement = outpatternelement;
    }
    public InPattern getInpattern() {
        return inpattern;
    }

    public void setInpattern(InPattern inpattern) {
        this.inpattern = inpattern;
    }
    public List<OclModel> getOclmodels() {
        return oclmodels;
    }

    public void addOclmodel(Oclmodel oclmodel) {
        this.oclmodels.add(oclmodel);
    }

}