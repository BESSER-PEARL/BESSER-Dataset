





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInstanceSpecification extends uml_TracedDeploymentTarget, uml_TracedPackageableElement, uml_TracedDeployedArtifact {






    private uml_TracedValueSpecification uml_tracedvaluespecification;




    private List<uml_TracedSlot> uml_tracedslots;


    public umlTrace_uml_TracedInstanceSpecification(
    ) {
        super(
        );
        this.uml_tracedslots = new ArrayList<>();
    }

    public umlTrace_uml_TracedInstanceSpecification(
        ArrayList<uml_TracedSlot> uml_tracedslots    ) {
        this.uml_tracedslots = uml_tracedslots;
    }


    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }
    public List<uml_TracedSlot> getUml_tracedslots() {
        return uml_tracedslots;
    }

    public void addUml_tracedslot(Uml_tracedslot uml_tracedslot) {
        this.uml_tracedslots.add(uml_tracedslot);
    }

}