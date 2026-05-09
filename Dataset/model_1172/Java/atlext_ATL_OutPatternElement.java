





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_OutPatternElement extends PatternElement {






    private InPatternElement inpatternelement;




    private OutPattern outpattern;




    private OclModel oclmodel;


    public atlext_ATL_OutPatternElement(
    ) {
        super(
        );
    }



    public InPatternElement getInpatternelement() {
        return inpatternelement;
    }

    public void setInpatternelement(InPatternElement inpatternelement) {
        this.inpatternelement = inpatternelement;
    }
    public OutPattern getOutpattern() {
        return outpattern;
    }

    public void setOutpattern(OutPattern outpattern) {
        this.outpattern = outpattern;
    }
    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }

}