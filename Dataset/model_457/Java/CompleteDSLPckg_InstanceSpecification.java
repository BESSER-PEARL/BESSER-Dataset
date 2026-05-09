





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_InstanceSpecification extends PackageableElement {






    private List<CompleteDSLPckg_Slot> completedslpckg_slots;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private CompleteDSLPckg_Slot completedslpckg_slot;


    public CompleteDSLPckg_InstanceSpecification(
    ) {
        super(
        );
        this.completedslpckg_slots = new ArrayList<>();
        this.completedslpckg_classifiers = new ArrayList<>();
    }

    public CompleteDSLPckg_InstanceSpecification(
        ArrayList<CompleteDSLPckg_Slot> completedslpckg_slots,        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers    ) {
        this.completedslpckg_slots = completedslpckg_slots;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
    }


    public List<CompleteDSLPckg_Slot> getCompletedslpckg_slots() {
        return completedslpckg_slots;
    }

    public void addCompletedslpckg_slot(Completedslpckg_slot completedslpckg_slot) {
        this.completedslpckg_slots.add(completedslpckg_slot);
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public CompleteDSLPckg_Slot getCompletedslpckg_slot() {
        return completedslpckg_slot;
    }

    public void setCompletedslpckg_slot(CompleteDSLPckg_Slot completedslpckg_slot) {
        this.completedslpckg_slot = completedslpckg_slot;
    }

}