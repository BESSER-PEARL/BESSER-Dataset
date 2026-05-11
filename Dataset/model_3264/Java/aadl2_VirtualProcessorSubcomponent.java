





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualProcessorSubcomponent extends VirtualProcessor, Subcomponent {






    private aadl2_ProcessorImplementation aadl2_processorimplementation;




    private aadl2_SystemImplementation aadl2_systemimplementation;




    private aadl2_VirtualProcessorSubcomponentType aadl2_virtualprocessorsubcomponenttype;




    private aadl2_VirtualProcessorImplementation aadl2_virtualprocessorimplementation;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_VirtualProcessorSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_ProcessorImplementation getAadl2_processorimplementation() {
        return aadl2_processorimplementation;
    }

    public void setAadl2_processorimplementation(aadl2_ProcessorImplementation aadl2_processorimplementation) {
        this.aadl2_processorimplementation = aadl2_processorimplementation;
    }
    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }
    public aadl2_VirtualProcessorSubcomponentType getAadl2_virtualprocessorsubcomponenttype() {
        return aadl2_virtualprocessorsubcomponenttype;
    }

    public void setAadl2_virtualprocessorsubcomponenttype(aadl2_VirtualProcessorSubcomponentType aadl2_virtualprocessorsubcomponenttype) {
        this.aadl2_virtualprocessorsubcomponenttype = aadl2_virtualprocessorsubcomponenttype;
    }
    public aadl2_VirtualProcessorImplementation getAadl2_virtualprocessorimplementation() {
        return aadl2_virtualprocessorimplementation;
    }

    public void setAadl2_virtualprocessorimplementation(aadl2_VirtualProcessorImplementation aadl2_virtualprocessorimplementation) {
        this.aadl2_virtualprocessorimplementation = aadl2_virtualprocessorimplementation;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}