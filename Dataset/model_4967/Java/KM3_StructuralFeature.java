





import java.util.List;
import java.util.ArrayList;

public class KM3_StructuralFeature extends ModelElement {

    private boolean isUnique;
    private int upper;
    private int lower;
    private boolean isOrdered;





    private KM3_Classifier km3_classifier;


    public KM3_StructuralFeature(
        boolean isUnique,        int upper,        int lower,        boolean isOrdered    ) {
        super(
        );
        this.isUnique = isUnique;
        this.upper = upper;
        this.lower = lower;
        this.isOrdered = isOrdered;
    }


    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }

    public KM3_Classifier getKm3_classifier() {
        return km3_classifier;
    }

    public void setKm3_classifier(KM3_Classifier km3_classifier) {
        this.km3_classifier = km3_classifier;
    }

}