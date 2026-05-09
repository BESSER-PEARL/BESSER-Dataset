





import java.util.List;
import java.util.ArrayList;

public class baseCST_MultiplicityBoundsCS extends MultiplicityCS {

    private String upperBound;
    private int lowerBound;



    public baseCST_MultiplicityBoundsCS(
        String upperBound,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }


}