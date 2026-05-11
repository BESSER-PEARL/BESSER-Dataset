





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementationReference extends Element {






    private aadl2_ComponentImplementation aadl2_componentimplementation;




    private aadl2_Subcomponent aadl2_subcomponent;


    public aadl2_ComponentImplementationReference(
    ) {
        super(
        );
    }



    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }

}