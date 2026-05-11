





import java.util.List;
import java.util.ArrayList;

public class sooml_StructuralFeature extends NamedElement {

    private int lowerBound;
    private int upperBound;



    public sooml_StructuralFeature(
        int lowerBound,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }


}