





import java.util.List;
import java.util.ArrayList;

public class aadl2_EndToEndFlow extends Flow, ModalPath, EndToEndFlowElement {






    private List<aadl2_EndToEndFlowElement> aadl2_endtoendflowelements;




    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private aadl2_EndToEndFlow aadl2_endtoendflow;


    public aadl2_EndToEndFlow(
    ) {
        super(
        );
        this.aadl2_endtoendflowelements = new ArrayList<>();
    }

    public aadl2_EndToEndFlow(
        ArrayList<aadl2_EndToEndFlowElement> aadl2_endtoendflowelements    ) {
        this.aadl2_endtoendflowelements = aadl2_endtoendflowelements;
    }


    public List<aadl2_EndToEndFlowElement> getAadl2_endtoendflowelements() {
        return aadl2_endtoendflowelements;
    }

    public void addAadl2_endtoendflowelement(Aadl2_endtoendflowelement aadl2_endtoendflowelement) {
        this.aadl2_endtoendflowelements.add(aadl2_endtoendflowelement);
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public aadl2_EndToEndFlow getAadl2_endtoendflow() {
        return aadl2_endtoendflow;
    }

    public void setAadl2_endtoendflow(aadl2_EndToEndFlow aadl2_endtoendflow) {
        this.aadl2_endtoendflow = aadl2_endtoendflow;
    }

}