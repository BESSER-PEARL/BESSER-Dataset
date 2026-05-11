





import java.util.List;
import java.util.ArrayList;

public class aadl2_ThreadGroupSubcomponent extends ThreadGroup, Subcomponent {






    private aadl2_ThreadGroupSubcomponentType aadl2_threadgroupsubcomponenttype;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;


    public aadl2_ThreadGroupSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_ThreadGroupSubcomponentType getAadl2_threadgroupsubcomponenttype() {
        return aadl2_threadgroupsubcomponenttype;
    }

    public void setAadl2_threadgroupsubcomponenttype(aadl2_ThreadGroupSubcomponentType aadl2_threadgroupsubcomponenttype) {
        this.aadl2_threadgroupsubcomponenttype = aadl2_threadgroupsubcomponenttype;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }

}