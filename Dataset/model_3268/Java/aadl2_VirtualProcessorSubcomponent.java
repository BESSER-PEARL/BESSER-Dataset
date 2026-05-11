





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualProcessorSubcomponent extends Subcomponent, VirtualProcessor {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_VirtualProcessorSubcomponentType aadl2_virtualprocessorsubcomponenttype;


    public aadl2_VirtualProcessorSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }
    public aadl2_VirtualProcessorSubcomponentType getAadl2_virtualprocessorsubcomponenttype() {
        return aadl2_virtualprocessorsubcomponenttype;
    }

    public void setAadl2_virtualprocessorsubcomponenttype(aadl2_VirtualProcessorSubcomponentType aadl2_virtualprocessorsubcomponenttype) {
        this.aadl2_virtualprocessorsubcomponenttype = aadl2_virtualprocessorsubcomponenttype;
    }

}