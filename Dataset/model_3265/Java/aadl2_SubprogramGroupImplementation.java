





import java.util.List;
import java.util.ArrayList;

public class aadl2_SubprogramGroupImplementation extends ComponentImplementation, SubprogramGroupClassifier {






    private List<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents;




    private List<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents;




    private List<aadl2_DataSubcomponent> aadl2_datasubcomponents;


    public aadl2_SubprogramGroupImplementation(
    ) {
        super(
        );
        this.aadl2_subprogramgroupsubcomponents = new ArrayList<>();
        this.aadl2_subprogramsubcomponents = new ArrayList<>();
        this.aadl2_datasubcomponents = new ArrayList<>();
    }

    public aadl2_SubprogramGroupImplementation(
        ArrayList<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents,        ArrayList<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents,        ArrayList<aadl2_DataSubcomponent> aadl2_datasubcomponents    ) {
        this.aadl2_subprogramgroupsubcomponents = aadl2_subprogramgroupsubcomponents;
        this.aadl2_subprogramsubcomponents = aadl2_subprogramsubcomponents;
        this.aadl2_datasubcomponents = aadl2_datasubcomponents;
    }


    public List<aadl2_SubprogramGroupSubcomponent> getAadl2_subprogramgroupsubcomponents() {
        return aadl2_subprogramgroupsubcomponents;
    }

    public void addAadl2_subprogramgroupsubcomponent(Aadl2_subprogramgroupsubcomponent aadl2_subprogramgroupsubcomponent) {
        this.aadl2_subprogramgroupsubcomponents.add(aadl2_subprogramgroupsubcomponent);
    }
    public List<aadl2_SubprogramSubcomponent> getAadl2_subprogramsubcomponents() {
        return aadl2_subprogramsubcomponents;
    }

    public void addAadl2_subprogramsubcomponent(Aadl2_subprogramsubcomponent aadl2_subprogramsubcomponent) {
        this.aadl2_subprogramsubcomponents.add(aadl2_subprogramsubcomponent);
    }
    public List<aadl2_DataSubcomponent> getAadl2_datasubcomponents() {
        return aadl2_datasubcomponents;
    }

    public void addAadl2_datasubcomponent(Aadl2_datasubcomponent aadl2_datasubcomponent) {
        this.aadl2_datasubcomponents.add(aadl2_datasubcomponent);
    }

}