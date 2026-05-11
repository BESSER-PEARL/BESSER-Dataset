





import java.util.List;
import java.util.ArrayList;

public class aadl2_SystemSubcomponent extends Subcomponent, System {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_SystemSubcomponentType aadl2_systemsubcomponenttype;




    private aadl2_SystemImplementation aadl2_systemimplementation;


    public aadl2_SystemSubcomponent(
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
    public aadl2_SystemSubcomponentType getAadl2_systemsubcomponenttype() {
        return aadl2_systemsubcomponenttype;
    }

    public void setAadl2_systemsubcomponenttype(aadl2_SystemSubcomponentType aadl2_systemsubcomponenttype) {
        this.aadl2_systemsubcomponenttype = aadl2_systemsubcomponenttype;
    }
    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }

}