





import java.util.List;
import java.util.ArrayList;

public class soopl_Property extends NamedElement {

    private boolean multiValued;
    private int upperBound;
    private int lowerBound;



    public soopl_Property(
        boolean multiValued,        int upperBound,        int lowerBound    ) {
        super(
        );
        this.multiValued = multiValued;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
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