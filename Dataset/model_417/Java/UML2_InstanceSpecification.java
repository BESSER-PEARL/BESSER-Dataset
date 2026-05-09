





import java.util.List;
import java.util.ArrayList;

public class UML2_InstanceSpecification extends PackageableElement, DeployedArtifact, DeploymentTarget {






    private List<UML2_Slot> uml2_slots;


    public UML2_InstanceSpecification(
    ) {
        super(
        );
        this.uml2_slots = new ArrayList<>();
    }

    public UML2_InstanceSpecification(
        ArrayList<UML2_Slot> uml2_slots    ) {
        this.uml2_slots = uml2_slots;
    }


    public List<UML2_Slot> getUml2_slots() {
        return uml2_slots;
    }

    public void addUml2_slot(Uml2_slot uml2_slot) {
        this.uml2_slots.add(uml2_slot);
    }

}