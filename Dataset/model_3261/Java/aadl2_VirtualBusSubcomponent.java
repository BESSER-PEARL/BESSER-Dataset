





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualBusSubcomponent extends Subcomponent, VirtualBus {






    private aadl2_VirtualProcessorImplementation aadl2_virtualprocessorimplementation;




    private aadl2_VirtualBusImplementation aadl2_virtualbusimplementation;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_VirtualBusSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_VirtualProcessorImplementation getAadl2_virtualprocessorimplementation() {
        return aadl2_virtualprocessorimplementation;
    }

    public void setAadl2_virtualprocessorimplementation(aadl2_VirtualProcessorImplementation aadl2_virtualprocessorimplementation) {
        this.aadl2_virtualprocessorimplementation = aadl2_virtualprocessorimplementation;
    }
    public aadl2_VirtualBusImplementation getAadl2_virtualbusimplementation() {
        return aadl2_virtualbusimplementation;
    }

    public void setAadl2_virtualbusimplementation(aadl2_VirtualBusImplementation aadl2_virtualbusimplementation) {
        this.aadl2_virtualbusimplementation = aadl2_virtualbusimplementation;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}