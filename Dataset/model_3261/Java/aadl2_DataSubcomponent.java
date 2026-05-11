





import java.util.List;
import java.util.ArrayList;

public class aadl2_DataSubcomponent extends PortConnectionEnd, Subcomponent, Data, ParameterConnectionEnd, AccessConnectionEnd {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_SubprogramImplementation aadl2_subprogramimplementation;




    private aadl2_ThreadImplementation aadl2_threadimplementation;




    private aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation;


    public aadl2_DataSubcomponent(
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
    public aadl2_SubprogramImplementation getAadl2_subprogramimplementation() {
        return aadl2_subprogramimplementation;
    }

    public void setAadl2_subprogramimplementation(aadl2_SubprogramImplementation aadl2_subprogramimplementation) {
        this.aadl2_subprogramimplementation = aadl2_subprogramimplementation;
    }
    public aadl2_ThreadImplementation getAadl2_threadimplementation() {
        return aadl2_threadimplementation;
    }

    public void setAadl2_threadimplementation(aadl2_ThreadImplementation aadl2_threadimplementation) {
        this.aadl2_threadimplementation = aadl2_threadimplementation;
    }
    public aadl2_ThreadGroupImplementation getAadl2_threadgroupimplementation() {
        return aadl2_threadgroupimplementation;
    }

    public void setAadl2_threadgroupimplementation(aadl2_ThreadGroupImplementation aadl2_threadgroupimplementation) {
        this.aadl2_threadgroupimplementation = aadl2_threadgroupimplementation;
    }

}