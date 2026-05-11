





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessSubcomponent extends Process, Subcomponent {






    private aadl2_ProcessSubcomponentType aadl2_processsubcomponenttype;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_ProcessSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_ProcessSubcomponentType getAadl2_processsubcomponenttype() {
        return aadl2_processsubcomponenttype;
    }

    public void setAadl2_processsubcomponenttype(aadl2_ProcessSubcomponentType aadl2_processsubcomponenttype) {
        this.aadl2_processsubcomponenttype = aadl2_processsubcomponenttype;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}