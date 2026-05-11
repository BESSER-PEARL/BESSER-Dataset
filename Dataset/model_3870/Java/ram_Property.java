





import java.util.List;
import java.util.ArrayList;

public class ram_Property extends StructuralFeature {

    private int upperBound;
    private String referenceType;
    private int lowerBound;



    public ram_Property(
        int upperBound,        String referenceType,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.referenceType = referenceType;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public String getReferencetype() {
        return referenceType;
    }

    public void setReferencetype(String referenceType) {
        this.referenceType = referenceType;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }


}