





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_OutPatternElement extends PatternElement {






    private OutPattern outpattern;




    private InPatternElement inpatternelement;




    private OclModel oclmodel;


    public atlstatic_ATL_OutPatternElement(
    ) {
        super(
        );
    }



    public OutPattern getOutpattern() {
        return outpattern;
    }

    public void setOutpattern(OutPattern outpattern) {
        this.outpattern = outpattern;
    }
    public InPatternElement getInpatternelement() {
        return inpatternelement;
    }

    public void setInpatternelement(InPatternElement inpatternelement) {
        this.inpatternelement = inpatternelement;
    }
    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }

}