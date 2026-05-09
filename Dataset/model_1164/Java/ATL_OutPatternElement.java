





import java.util.List;
import java.util.ArrayList;

public class ATL_OutPatternElement extends PatternElement {






    private OutPattern outpattern;




    private InPatternElement inpatternelement;




    private OclModel oclmodel;


    public ATL_OutPatternElement(
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