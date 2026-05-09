





import java.util.List;
import java.util.ArrayList;

public class UML2_Slot extends Element {






    private UML2_StructuralFeature uml2_structuralfeature;




    private List<UML2_ValueSpecification> uml2_valuespecifications;


    public UML2_Slot(
    ) {
        super(
        );
        this.uml2_valuespecifications = new ArrayList<>();
    }

    public UML2_Slot(
        ArrayList<UML2_ValueSpecification> uml2_valuespecifications    ) {
        this.uml2_valuespecifications = uml2_valuespecifications;
    }


    public UML2_StructuralFeature getUml2_structuralfeature() {
        return uml2_structuralfeature;
    }

    public void setUml2_structuralfeature(UML2_StructuralFeature uml2_structuralfeature) {
        this.uml2_structuralfeature = uml2_structuralfeature;
    }
    public List<UML2_ValueSpecification> getUml2_valuespecifications() {
        return uml2_valuespecifications;
    }

    public void addUml2_valuespecification(Uml2_valuespecification uml2_valuespecification) {
        this.uml2_valuespecifications.add(uml2_valuespecification);
    }

}