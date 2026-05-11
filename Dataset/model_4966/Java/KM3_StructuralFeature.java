





import java.util.List;
import java.util.ArrayList;

public class KM3_StructuralFeature extends ModelElement {

    private int upper;
    private boolean isUnique;
    private int lower;
    private boolean isOrdered;





    private KM3_Class km3_class;




    private KM3_Class km3_class;


    public KM3_StructuralFeature(
        int upper,        boolean isUnique,        int lower,        boolean isOrdered    ) {
        super(
        );
        this.upper = upper;
        this.isUnique = isUnique;
        this.lower = lower;
        this.isOrdered = isOrdered;
    }


    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
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

}