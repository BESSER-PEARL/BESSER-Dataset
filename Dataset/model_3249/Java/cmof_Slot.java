





import java.util.List;
import java.util.ArrayList;

public class cmof_Slot extends Element {






    private List<cmof_ValueSpecification> cmof_valuespecifications;




    private cmof_StructuralFeature cmof_structuralfeature;


    public cmof_Slot(
    ) {
        super(
        );
        this.cmof_valuespecifications = new ArrayList<>();
    }

    public cmof_Slot(
        ArrayList<cmof_ValueSpecification> cmof_valuespecifications    ) {
        this.cmof_valuespecifications = cmof_valuespecifications;
    }


    public List<cmof_ValueSpecification> getCmof_valuespecifications() {
        return cmof_valuespecifications;
    }

    public void addCmof_valuespecification(Cmof_valuespecification cmof_valuespecification) {
        this.cmof_valuespecifications.add(cmof_valuespecification);
    }
    public cmof_StructuralFeature getCmof_structuralfeature() {
        return cmof_structuralfeature;
    }

    public void setCmof_structuralfeature(cmof_StructuralFeature cmof_structuralfeature) {
        this.cmof_structuralfeature = cmof_structuralfeature;
    }

}