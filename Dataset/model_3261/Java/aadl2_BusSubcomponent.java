





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusSubcomponent extends Bus, Subcomponent, AccessConnectionEnd {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_BusSubcomponent(
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

}