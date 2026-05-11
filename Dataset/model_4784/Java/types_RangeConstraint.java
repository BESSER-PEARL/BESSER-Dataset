





import java.util.List;
import java.util.ArrayList;

public class types_RangeConstraint extends TypeConstraint {

    private String lowerBound;
    private String upperBound;



    public types_RangeConstraint(
        String lowerBound,        String upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }


}