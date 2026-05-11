





import java.util.List;
import java.util.ArrayList;

public class aadl2_Subcomponent extends Context, StructuralFeature, ArrayableElement, ModalElement, FlowElement {

    private String allModes;





    private aadl2_Subcomponent aadl2_subcomponent;


    public aadl2_Subcomponent(
        String allModes    ) {
        super(
        );
        this.allModes = allModes;
    }


    public String getAllmodes() {
        return allModes;
    }

    public void setAllmodes(String allModes) {
        this.allModes = allModes;
    }

    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }

}