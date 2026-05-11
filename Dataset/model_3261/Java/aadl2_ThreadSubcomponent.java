





import java.util.List;
import java.util.ArrayList;

public class aadl2_ThreadSubcomponent extends Thread, Subcomponent {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation;


    public aadl2_ThreadSubcomponent(
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
    public aadl2_ThreadGroupImplementation getAadl2_threadgroupimplementation() {
        return aadl2_threadgroupimplementation;
    }

    public void setAadl2_threadgroupimplementation(aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation) {
        this.aadl2_threadgroupimplementation = aadl2_threadgroupimplementation;
    }

}