





import java.util.List;
import java.util.ArrayList;

public class aadl2_ThreadSubcomponent extends Thread, Subcomponent {






    private aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation;




    private aadl2_ProcessImplementation aadl2_processimplementation;




    private aadl2_ThreadClassifier aadl2_threadclassifier;


    public aadl2_ThreadSubcomponent(
    ) {
        super(
        );
    }



    public aadl2_ThreadGroupImplementation getAadl2_threadgroupimplementation() {
        return aadl2_threadgroupimplementation;
    }

    public void setAadl2_threadgroupimplementation(aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation) {
        this.aadl2_threadgroupimplementation = aadl2_threadgroupimplementation;
    }
    public aadl2_ProcessImplementation getAadl2_processimplementation() {
        return aadl2_processimplementation;
    }

    public void setAadl2_processimplementation(aadl2_ProcessImplementation aadl2_processimplementation) {
        this.aadl2_processimplementation = aadl2_processimplementation;
    }
    public aadl2_ThreadClassifier getAadl2_threadclassifier() {
        return aadl2_threadclassifier;
    }

    public void setAadl2_threadclassifier(aadl2_ThreadClassifier aadl2_threadclassifier) {
        this.aadl2_threadclassifier = aadl2_threadclassifier;
    }

}