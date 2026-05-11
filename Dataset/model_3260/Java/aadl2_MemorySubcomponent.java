





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemorySubcomponent extends Memory, Subcomponent {






    private aadl2_SystemImplementation aadl2_systemimplementation;




    private aadl2_MemoryImplementation aadl2_memoryimplementation;




    private aadl2_MemoryClassifier aadl2_memoryclassifier;




    private aadl2_ProcessorImplementation aadl2_processorimplementation;


    public aadl2_MemorySubcomponent(
    ) {
        super(
        );
    }



    public aadl2_SystemImplementation getAadl2_systemimplementation() {
        return aadl2_systemimplementation;
    }

    public void setAadl2_systemimplementation(aadl2_SystemImplementation aadl2_systemimplementation) {
        this.aadl2_systemimplementation = aadl2_systemimplementation;
    }
    public aadl2_MemoryImplementation getAadl2_memoryimplementation() {
        return aadl2_memoryimplementation;
    }

    public void setAadl2_memoryimplementation(aadl2_MemoryImplementation aadl2_memoryimplementation) {
        this.aadl2_memoryimplementation = aadl2_memoryimplementation;
    }
    public aadl2_MemoryClassifier getAadl2_memoryclassifier() {
        return aadl2_memoryclassifier;
    }

    public void setAadl2_memoryclassifier(aadl2_MemoryClassifier aadl2_memoryclassifier) {
        this.aadl2_memoryclassifier = aadl2_memoryclassifier;
    }
    public aadl2_ProcessorImplementation getAadl2_processorimplementation() {
        return aadl2_processorimplementation;
    }

    public void setAadl2_processorimplementation(aadl2_ProcessorImplementation aadl2_processorimplementation) {
        this.aadl2_processorimplementation = aadl2_processorimplementation;
    }

}