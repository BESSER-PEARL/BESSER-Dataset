





import java.util.List;
import java.util.ArrayList;

public class KM3_StructuralFeature extends TypedElement {






    private KM3_Class km3_class;




    private KM3_Class km3_class;




    private List<KM3_StructuralFeature> km3_structuralfeatures;




    private KM3_StructuralFeature km3_structuralfeature;


    public KM3_StructuralFeature(
    ) {
        super(
        );
        this.km3_structuralfeatures = new ArrayList<>();
    }

    public KM3_StructuralFeature(
        ArrayList<KM3_StructuralFeature> km3_structuralfeatures    ) {
        this.km3_structuralfeatures = km3_structuralfeatures;
    }


    public KM3_Class getKm3_class() {
        return km3_class;
    }

    public void setKm3_class(KM3_Class km3_class) {
        this.km3_class = km3_class;
    }
    public KM3_Class getKm3_class() {
        return km3_class;
    }

    public void setKm3_class(KM3_Class km3_class) {
        this.km3_class = km3_class;
    }
    public List<KM3_StructuralFeature> getKm3_structuralfeatures() {
        return km3_structuralfeatures;
    }

    public void addKm3_structuralfeature(Km3_structuralfeature km3_structuralfeature) {
        this.km3_structuralfeatures.add(km3_structuralfeature);
    }
    public KM3_StructuralFeature getKm3_structuralfeature() {
        return km3_structuralfeature;
    }

    public void setKm3_structuralfeature(KM3_StructuralFeature km3_structuralfeature) {
        this.km3_structuralfeature = km3_structuralfeature;
    }

}