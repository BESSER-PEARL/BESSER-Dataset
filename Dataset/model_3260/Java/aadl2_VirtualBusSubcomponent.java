





import java.util.List;
import java.util.ArrayList;

public class aadl2_VirtualBusSubcomponent extends VirtualBus, Subcomponent {






    private aadl2_BusImplementation aadl2_busimplementation;


    public aadl2_VirtualBusSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_BusImplementation getAadl2_busimplementation() {
        return aadl2_busimplementation;
    }

    public void setAadl2_busimplementation(aadl2_BusImplementation aadl2_busimplementation) {
        this.aadl2_busimplementation = aadl2_busimplementation;
    }

}