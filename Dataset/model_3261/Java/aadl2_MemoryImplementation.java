





import java.util.List;
import java.util.ArrayList;

public class aadl2_MemoryImplementation extends ComponentImplementation, MemoryClassifier {






    private List<aadl2_BusSubcomponent> aadl2_bussubcomponents;




    private List<aadl2_MemorySubcomponent> aadl2_memorysubcomponents;


    public aadl2_MemoryImplementation(
    ) {
        super(
        );
        this.aadl2_bussubcomponents = new ArrayList<>();
        this.aadl2_memorysubcomponents = new ArrayList<>();
    }

    public aadl2_MemoryImplementation(
        ArrayList<aadl2_BusSubcomponent> aadl2_bussubcomponents,        ArrayList<aadl2_MemorySubcomponent> aadl2_memorysubcomponents    ) {
        this.aadl2_bussubcomponents = aadl2_bussubcomponents;
        this.aadl2_memorysubcomponents = aadl2_memorysubcomponents;
    }


    public List<aadl2_BusSubcomponent> getAadl2_bussubcomponents() {
        return aadl2_bussubcomponents;
    }

    public void addAadl2_bussubcomponent(Aadl2_bussubcomponent aadl2_bussubcomponent) {
        this.aadl2_bussubcomponents.add(aadl2_bussubcomponent);
    }
    public List<aadl2_MemorySubcomponent> getAadl2_memorysubcomponents() {
        return aadl2_memorysubcomponents;
    }

    public void addAadl2_memorysubcomponent(Aadl2_memorysubcomponent aadl2_memorysubcomponent) {
        this.aadl2_memorysubcomponents.add(aadl2_memorysubcomponent);
    }

}