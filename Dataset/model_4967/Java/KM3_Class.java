





import java.util.List;
import java.util.ArrayList;

public class KM3_Class extends Classifier {

    private boolean isAbstract;





    private List<KM3_StructuralFeature> km3_structuralfeatures;




    private List<KM3_Class> km3_classs;




    private KM3_StructuralFeature km3_structuralfeature;


    public KM3_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.km3_structuralfeatures = new ArrayList<>();
        this.km3_classs = new ArrayList<>();
    }

    public KM3_Class(
        boolean isAbstract        ArrayList<KM3_StructuralFeature> km3_structuralfeatures,        ArrayList<KM3_Class> km3_classs    ) {
        this.isAbstract = isAbstract;
        this.km3_structuralfeatures = km3_structuralfeatures;
        this.km3_classs = km3_classs;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<KM3_StructuralFeature> getKm3_structuralfeatures() {
        return km3_structuralfeatures;
    }

    public void addKm3_structuralfeature(Km3_structuralfeature km3_structuralfeature) {
        this.km3_structuralfeatures.add(km3_structuralfeature);
    }
    public List<KM3_Class> getKm3_classs() {
        return km3_classs;
    }

    public void addKm3_class(Km3_class km3_class) {
        this.km3_classs.add(km3_class);
    }
    public KM3_StructuralFeature getKm3_structuralfeature() {
        return km3_structuralfeature;
    }

    public void setKm3_structuralfeature(KM3_StructuralFeature km3_structuralfeature) {
        this.km3_structuralfeature = km3_structuralfeature;
    }

}