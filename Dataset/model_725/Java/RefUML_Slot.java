





import java.util.List;
import java.util.ArrayList;

public class RefUML_Slot extends Element {






    private List<RefUML_ValueSpecification> refuml_valuespecifications;




    private RefUML_StructuralFeature refuml_structuralfeature;


    public RefUML_Slot(
    ) {
        super(
        );
        this.refuml_valuespecifications = new ArrayList<>();
    }

    public RefUML_Slot(
        ArrayList<RefUML_ValueSpecification> refuml_valuespecifications    ) {
        this.refuml_valuespecifications = refuml_valuespecifications;
    }


    public List<RefUML_ValueSpecification> getRefuml_valuespecifications() {
        return refuml_valuespecifications;
    }

    public void addRefuml_valuespecification(Refuml_valuespecification refuml_valuespecification) {
        this.refuml_valuespecifications.add(refuml_valuespecification);
    }
    public RefUML_StructuralFeature getRefuml_structuralfeature() {
        return refuml_structuralfeature;
    }

    public void setRefuml_structuralfeature(RefUML_StructuralFeature refuml_structuralfeature) {
        this.refuml_structuralfeature = refuml_structuralfeature;
    }

}