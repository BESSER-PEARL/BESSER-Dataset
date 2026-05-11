





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessImplementation extends ComponentImplementation, ProcessClassifier {






    private List<aadl2_ThreadGroupSubcomponent> aadl2_threadgroupsubcomponents;


    public aadl2_ProcessImplementation(
    ) {
        super(
        );
        this.aadl2_threadgroupsubcomponents = new ArrayList<>();
    }

    public aadl2_ProcessImplementation(
        ArrayList<aadl2_ThreadGroupSubcomponent> aadl2_threadgroupsubcomponents    ) {
        this.aadl2_threadgroupsubcomponents = aadl2_threadgroupsubcomponents;
    }


    public List<aadl2_ThreadGroupSubcomponent> getAadl2_threadgroupsubcomponents() {
        return aadl2_threadgroupsubcomponents;
    }

    public void addAadl2_threadgroupsubcomponent(Aadl2_threadgroupsubcomponent aadl2_threadgroupsubcomponent) {
        this.aadl2_threadgroupsubcomponents.add(aadl2_threadgroupsubcomponent);
    }

}