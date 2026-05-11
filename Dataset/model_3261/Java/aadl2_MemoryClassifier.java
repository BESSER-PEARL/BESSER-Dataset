





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemoryClassifier extends Memory, ComponentClassifier {






    private aadl2_MemorySubcomponent aadl2_memorysubcomponent;


    public aadl2_MemoryClassifier(
    ) {
        super(
        );
    }



    public aadl2_MemorySubcomponent getAadl2_memorysubcomponent() {
        return aadl2_memorysubcomponent;
    }

    public void setAadl2_memorysubcomponent(aadl2_MemorySubcomponent aadl2_memorysubcomponent) {
        this.aadl2_memorysubcomponent = aadl2_memorysubcomponent;
    }

}