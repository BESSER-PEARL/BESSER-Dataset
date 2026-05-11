





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemorySubcomponent extends Subcomponent, Memory {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_SystemImplementation aadl2_systemimplementation;




    private aadl2_ProcessorImplementation aadl2_processorimplementation;




    private aadl2_MemorySubcomponentType aadl2_memorysubcomponenttype;




    private aadl2_MemoryImplementation aadl2_memoryimplementation;


    public aadl2_MemorySubcomponent(
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
    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }
    public aadl2_ProcessorImplementation getAadl2_processorimplementation() {
        return aadl2_processorimplementation;
    }

    public void setAadl2_processorimplementation(aadl2_ProcessorImplementation aadl2_processorimplementation) {
        this.aadl2_processorimplementation = aadl2_processorimplementation;
    }
    public aadl2_MemorySubcomponentType getAadl2_memorysubcomponenttype() {
        return aadl2_memorysubcomponenttype;
    }

    public void setAadl2_memorysubcomponenttype(aadl2_MemorySubcomponentType aadl2_memorysubcomponenttype) {
        this.aadl2_memorysubcomponenttype = aadl2_memorysubcomponenttype;
    }
    public aadl2_MemoryImplementation getAadl2_memoryimplementation() {
        return aadl2_memoryimplementation;
    }

    public void setAadl2_memoryimplementation(aadl2_MemoryImplementation aadl2_memoryimplementation) {
        this.aadl2_memoryimplementation = aadl2_memoryimplementation;
    }

}