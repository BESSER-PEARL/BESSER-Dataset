





import java.util.List;
import java.util.ArrayList;

public class ram_Property extends StructuralFeature {

    private String referenceType;
    private int upperBound;
    private int lowerBound;



    public ram_Property(
        String referenceType,        int upperBound,        int lowerBound    ) {
        super(
        );
        this.referenceType = referenceType;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public String getReferencetype() {
        return referenceType;
    }

    public void setReferencetype(String referenceType) {
        this.referenceType = referenceType;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }


}