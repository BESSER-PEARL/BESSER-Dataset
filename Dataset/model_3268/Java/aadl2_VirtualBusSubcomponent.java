





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualBusSubcomponent extends AccessConnectionEnd, VirtualBus, Subcomponent {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_VirtualBusSubcomponentType aadl2_virtualbussubcomponenttype;


    public aadl2_VirtualBusSubcomponent(
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
    public aadl2_VirtualBusSubcomponentType getAadl2_virtualbussubcomponenttype() {
        return aadl2_virtualbussubcomponenttype;
    }

    public void setAadl2_virtualbussubcomponenttype(aadl2_VirtualBusSubcomponentType aadl2_virtualbussubcomponenttype) {
        this.aadl2_virtualbussubcomponenttype = aadl2_virtualbussubcomponenttype;
    }

}