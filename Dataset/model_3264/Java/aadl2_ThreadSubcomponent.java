





import java.util.List;
import java.util.ArrayList;

public class aadl2_ThreadSubcomponent extends Subcomponent, Thread {






    private aadl2_ThreadSubcomponentType aadl2_threadsubcomponenttype;




    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_ProcessImplementation aadl2_processimplementation;




    private aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation;


    public aadl2_ThreadSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_ThreadSubcomponentType getAadl2_threadsubcomponenttype() {
        return aadl2_threadsubcomponenttype;
    }

    public void setAadl2_threadsubcomponenttype(aadl2_ThreadSubcomponentType aadl2_threadsubcomponenttype) {
        this.aadl2_threadsubcomponenttype = aadl2_threadsubcomponenttype;
    }
    public aadl2_AbstractImplementation getAadl2_abstractimplementation() {
        return aadl2_abstractimplementation;
    }

    public void setAadl2_abstractimplementation(aadl2_AbstractImplementation aadl2_abstractimplementation) {
        this.aadl2_abstractimplementation = aadl2_abstractimplementation;
    }
    public aadl2_ProcessImplementation getAadl2_processimplementation() {
        return aadl2_processimplementation;
    }

    public void setAadl2_processimplementation(aadl2_ProcessImplementation aadl2_processimplementation) {
        this.aadl2_processimplementation = aadl2_processimplementation;
    }
    public aadl2_ThreadGroupImplementation getAadl2_threadgroupimplementation() {
        return aadl2_threadgroupimplementation;
    }

    public void setAadl2_threadgroupimplementation(aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation) {
        this.aadl2_threadgroupimplementation = aadl2_threadgroupimplementation;
    }

}