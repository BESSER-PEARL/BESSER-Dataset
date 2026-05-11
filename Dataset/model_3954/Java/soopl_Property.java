





import java.util.List;
import java.util.ArrayList;

public class soopl_Property extends NamedElement {

    private int upperBound;
    private boolean multiValued;
    private int lowerBound;





    private soopl_Class soopl_class;


    public soopl_Property(
        int upperBound,        boolean multiValued,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.multiValued = multiValued;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public soopl_Class getSoopl_class() {
        return soopl_class;
    }

    public void setSoopl_class(soopl_Class soopl_class) {
        this.soopl_class = soopl_class;
    }

}