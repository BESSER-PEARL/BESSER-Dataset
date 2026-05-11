





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedSlot extends TracedElement {






    private List<uml_TracedValueSpecification> uml_tracedvaluespecifications;




    private uml_TracedStructuralFeature uml_tracedstructuralfeature;




    private uml_TracedInstanceSpecification uml_tracedinstancespecification;


    public umlTrace_uml_TracedSlot(
    ) {
        super(
        );
        this.uml_tracedvaluespecifications = new ArrayList<>();
    }

    public umlTrace_uml_TracedSlot(
        ArrayList<uml_TracedValueSpecification> uml_tracedvaluespecifications    ) {
        this.uml_tracedvaluespecifications = uml_tracedvaluespecifications;
    }


    public List<uml_TracedValueSpecification> getUml_tracedvaluespecifications() {
        return uml_tracedvaluespecifications;
    }

    public void addUml_tracedvaluespecification(Uml_tracedvaluespecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecifications.add(uml_tracedvaluespecification);
    }
    public uml_TracedStructuralFeature getUml_tracedstructuralfeature() {
        return uml_tracedstructuralfeature;
    }

    public void setUml_tracedstructuralfeature(uml_TracedStructuralFeature uml_tracedstructuralfeature) {
        this.uml_tracedstructuralfeature = uml_tracedstructuralfeature;
    }
    public uml_TracedInstanceSpecification getUml_tracedinstancespecification() {
        return uml_tracedinstancespecification;
    }

    public void setUml_tracedinstancespecification(uml_TracedInstanceSpecification uml_tracedinstancespecification) {
        this.uml_tracedinstancespecification = uml_tracedinstancespecification;
    }

}