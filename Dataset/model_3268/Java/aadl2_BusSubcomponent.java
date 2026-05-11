





import java.util.List;
import java.util.ArrayList;

public class aadl2_BusSubcomponent extends AccessConnectionEnd, Subcomponent, Bus {






    private aadl2_BusSubcomponentType aadl2_bussubcomponenttype;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_BusSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_BusSubcomponentType getAadl2_bussubcomponenttype() {
        return aadl2_bussubcomponenttype;
    }

    public void setAadl2_bussubcomponenttype(aadl2_BusSubcomponentType aadl2_bussubcomponenttype) {
        this.aadl2_bussubcomponenttype = aadl2_bussubcomponenttype;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}