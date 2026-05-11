





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessorSubcomponent extends Processor, Subcomponent {






    private aadl2_SystemImplementation aadl2_systemimplementation;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_ProcessorSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}