





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowSegment extends Element {






    private aadl2_Context aadl2_context;




    private aadl2_FlowImplementation aadl2_flowimplementation;




    private aadl2_FlowElement aadl2_flowelement;


    public aadl2_FlowSegment(
    ) {
        super(
        );
    }



    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }
    public aadl2_FlowImplementation getAadl2_flowimplementation() {
        return aadl2_flowimplementation;
    }

    public void setAadl2_flowimplementation(aadl2_FlowImplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementation = aadl2_flowimplementation;
    }
    public aadl2_FlowElement getAadl2_flowelement() {
        return aadl2_flowelement;
    }

    public void setAadl2_flowelement(aadl2_FlowElement aadl2_flowelement) {
        this.aadl2_flowelement = aadl2_flowelement;
    }

}