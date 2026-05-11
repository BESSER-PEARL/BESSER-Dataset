





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupSubcomponent extends AccessConnectionEnd, Subcomponent, SubprogramGroup, CallContext {






    private aadl2_SubprogramGroupSubcomponentType aadl2_subprogramgroupsubcomponenttype;




    private aadl2_ThreadImplementation aadl2_threadimplementation;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_SubprogramGroupSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_SubprogramGroupSubcomponentType getAadl2_subprogramgroupsubcomponenttype() {
        return aadl2_subprogramgroupsubcomponenttype;
    }

    public void setAadl2_subprogramgroupsubcomponenttype(aadl2_SubprogramGroupSubcomponentType aadl2_subprogramgroupsubcomponenttype) {
        this.aadl2_subprogramgroupsubcomponenttype = aadl2_subprogramgroupsubcomponenttype;
    }
    public aadl2_ThreadImplementation getAadl2_threadimplementation() {
        return aadl2_threadimplementation;
    }

    public void setAadl2_threadimplementation(aadl2_ThreadImplementation aadl2_threadimplementation) {
        this.aadl2_threadimplementation = aadl2_threadimplementation;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}