





import java.util.List;
import java.util.ArrayList;

public class top_ATL_OutPatternElement extends PatternElement {






    private OclModel oclmodel;




    private OutPattern outpattern;




    private InPatternElement inpatternelement;


    public top_ATL_OutPatternElement(
    ) {
        super(
        );
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
    public InPatternElement getInpatternelement() {
        return inpatternelement;
    }

    public void setInpatternelement(InPatternElement inpatternelement) {
        this.inpatternelement = inpatternelement;
    }

}