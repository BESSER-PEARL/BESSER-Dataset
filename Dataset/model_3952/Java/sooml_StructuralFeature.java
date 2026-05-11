





import java.util.List;
import java.util.ArrayList;

public class sooml_StructuralFeature extends NamedElement {

    private int lowerBound;
    private int upperBound;





    private sooml_Class sooml_class;


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

    public sooml_Class getSooml_class() {
        return sooml_class;
    }

    public void setSooml_class(sooml_Class sooml_class) {
        this.sooml_class = sooml_class;
    }

}