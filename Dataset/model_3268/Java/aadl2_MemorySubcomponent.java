





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemorySubcomponent extends Memory, Subcomponent {






    private aadl2_AbstractImplementation aadl2_abstractimplementation;




    private aadl2_MemorySubcomponentType aadl2_memorysubcomponenttype;


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
    public aadl2_MemorySubcomponentType getAadl2_memorysubcomponenttype() {
        return aadl2_memorysubcomponenttype;
    }

    public void setAadl2_memorysubcomponenttype(aadl2_MemorySubcomponentType aadl2_memorysubcomponenttype) {
        this.aadl2_memorysubcomponenttype = aadl2_memorysubcomponenttype;
    }

}