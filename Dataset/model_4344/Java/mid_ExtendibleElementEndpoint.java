





import java.util.List;
import java.util.ArrayList;

public class mid_ExtendibleElementEndpoint extends ExtendibleElement {

    private int upperBound;
    private int lowerBound;





    private mid_ExtendibleElement mid_extendibleelement;


    public mid_ExtendibleElementEndpoint(
        int upperBound,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
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

    public mid_ExtendibleElement getMid_extendibleelement() {
        return mid_extendibleelement;
    }

    public void setMid_extendibleelement(mid_ExtendibleElement mid_extendibleelement) {
        this.mid_extendibleelement = mid_extendibleelement;
    }

}