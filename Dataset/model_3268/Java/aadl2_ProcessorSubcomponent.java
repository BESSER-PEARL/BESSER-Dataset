





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessorSubcomponent extends Subcomponent, Processor {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_ProcessorSubcomponentType aadl2_processorsubcomponenttype;


    public aadl2_ProcessorSubcomponent(
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
    public aadl2_ProcessorSubcomponentType getAadl2_processorsubcomponenttype() {
        return aadl2_processorsubcomponenttype;
    }

    public void setAadl2_processorsubcomponenttype(aadl2_ProcessorSubcomponentType aadl2_processorsubcomponenttype) {
        this.aadl2_processorsubcomponenttype = aadl2_processorsubcomponenttype;
    }

}