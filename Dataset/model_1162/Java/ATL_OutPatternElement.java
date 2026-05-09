





import java.util.List;
import java.util.ArrayList;

public class ATL_OutPatternElement extends PatternElement {






    private InPatternElement inpatternelement;




    private OclModel oclmodel;




    private OutPattern outpattern;


    public ATL_OutPatternElement(
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
    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }
    public OutPattern getOutpattern() {
        return outpattern;
    }

    public void setOutpattern(OutPattern outpattern) {
        this.outpattern = outpattern;
    }

}