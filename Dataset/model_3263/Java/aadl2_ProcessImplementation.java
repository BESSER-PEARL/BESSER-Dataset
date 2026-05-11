





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessImplementation extends ProcessClassifier, ComponentImplementation {






    private List<aadl2_DataSubcomponent> aadl2_datasubcomponents;




    private List<aadl2_ThreadGroupSubcomponent> aadl2_threadgroupsubcomponents;




    private List<aadl2_ThreadSubcomponent> aadl2_threadsubcomponents;




    private List<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents;




    private List<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents;


    public aadl2_ProcessImplementation(
    ) {
        super(
        );
        this.aadl2_datasubcomponents = new ArrayList<>();
        this.aadl2_threadgroupsubcomponents = new ArrayList<>();
        this.aadl2_threadsubcomponents = new ArrayList<>();
        this.aadl2_subprogramsubcomponents = new ArrayList<>();
        this.aadl2_subprogramgroupsubcomponents = new ArrayList<>();
    }

    public aadl2_ProcessImplementation(
        ArrayList<aadl2_DataSubcomponent> aadl2_datasubcomponents,        ArrayList<aadl2_ThreadGroupSubcomponent> aadl2_threadgroupsubcomponents,        ArrayList<aadl2_ThreadSubcomponent> aadl2_threadsubcomponents,        ArrayList<aadl2_SubprogramSubcomponent> aadl2_subprogramsubcomponents,        ArrayList<aadl2_SubprogramGroupSubcomponent> aadl2_subprogramgroupsubcomponents    ) {
        this.aadl2_datasubcomponents = aadl2_datasubcomponents;
        this.aadl2_threadgroupsubcomponents = aadl2_threadgroupsubcomponents;
        this.aadl2_threadsubcomponents = aadl2_threadsubcomponents;
        this.aadl2_subprogramsubcomponents = aadl2_subprogramsubcomponents;
        this.aadl2_subprogramgroupsubcomponents = aadl2_subprogramgroupsubcomponents;
    }


    public List<aadl2_DataSubcomponent> getAadl2_datasubcomponents() {
        return aadl2_datasubcomponents;
    }

    public void addAadl2_datasubcomponent(Aadl2_datasubcomponent aadl2_datasubcomponent) {
        this.aadl2_datasubcomponents.add(aadl2_datasubcomponent);
    }
    public List<aadl2_ThreadGroupSubcomponent> getAadl2_threadgroupsubcomponents() {
        return aadl2_threadgroupsubcomponents;
    }

    public void addAadl2_threadgroupsubcomponent(Aadl2_threadgroupsubcomponent aadl2_threadgroupsubcomponent) {
        this.aadl2_threadgroupsubcomponents.add(aadl2_threadgroupsubcomponent);
    }
    public List<aadl2_ThreadSubcomponent> getAadl2_threadsubcomponents() {
        return aadl2_threadsubcomponents;
    }

    public void addAadl2_threadsubcomponent(Aadl2_threadsubcomponent aadl2_threadsubcomponent) {
        this.aadl2_threadsubcomponents.add(aadl2_threadsubcomponent);
    }
    public List<aadl2_SubprogramSubcomponent> getAadl2_subprogramsubcomponents() {
        return aadl2_subprogramsubcomponents;
    }

    public void addAadl2_subprogramsubcomponent(Aadl2_subprogramsubcomponent aadl2_subprogramsubcomponent) {
        this.aadl2_subprogramsubcomponents.add(aadl2_subprogramsubcomponent);
    }
    public List<aadl2_SubprogramGroupSubcomponent> getAadl2_subprogramgroupsubcomponents() {
        return aadl2_subprogramgroupsubcomponents;
    }

    public void addAadl2_subprogramgroupsubcomponent(Aadl2_subprogramgroupsubcomponent aadl2_subprogramgroupsubcomponent) {
        this.aadl2_subprogramgroupsubcomponents.add(aadl2_subprogramgroupsubcomponent);
    }

}