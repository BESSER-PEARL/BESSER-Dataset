





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubcomponentFlow extends FlowElement {






    private aadl2_FlowSpecification aadl2_flowspecification;




    private aadl2_Subcomponent aadl2_subcomponent;




    private aadl2_EndToEndFlow aadl2_endtoendflow;




    private aadl2_DataAccess aadl2_dataaccess;




    private aadl2_FlowImplementation aadl2_flowimplementation;


    public aadl2_SubcomponentFlow(
    ) {
        super(
        );
    }



    public aadl2_FlowSpecification getAadl2_flowspecification() {
        return aadl2_flowspecification;
    }

    public void setAadl2_flowspecification(aadl2_FlowSpecification aadl2_flowspecification) {
        this.aadl2_flowspecification = aadl2_flowspecification;
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public aadl2_EndToEndFlow getAadl2_endtoendflow() {
        return aadl2_endtoendflow;
    }

    public void setAadl2_endtoendflow(aadl2_EndToEndFlow aadl2_endtoendflow) {
        this.aadl2_endtoendflow = aadl2_endtoendflow;
    }
    public aadl2_DataAccess getAadl2_dataaccess() {
        return aadl2_dataaccess;
    }

    public void setAadl2_dataaccess(aadl2_DataAccess aadl2_dataaccess) {
        this.aadl2_dataaccess = aadl2_dataaccess;
    }
    public aadl2_FlowImplementation getAadl2_flowimplementation() {
        return aadl2_flowimplementation;
    }

    public void setAadl2_flowimplementation(aadl2_FlowImplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementation = aadl2_flowimplementation;
    }

}