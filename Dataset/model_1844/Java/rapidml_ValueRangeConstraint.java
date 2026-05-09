





import java.util.List;
import java.util.ArrayList;

public class rapidml_ValueRangeConstraint extends Constraint {

    private boolean maxValueExclusive;
    private String maxValue;
    private boolean minValueExclusive;
    private String minValue;



    public rapidml_ValueRangeConstraint(
        boolean maxValueExclusive,        String maxValue,        boolean minValueExclusive,        String minValue    ) {
        super(
        );
        this.maxValueExclusive = maxValueExclusive;
        this.maxValue = maxValue;
        this.minValueExclusive = minValueExclusive;
        this.minValue = minValue;
    }


    public boolean getMaxvalueexclusive() {
        return maxValueExclusive;
    }

    public void setMaxvalueexclusive(boolean maxValueExclusive) {
        this.maxValueExclusive = maxValueExclusive;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public boolean getMinvalueexclusive() {
        return minValueExclusive;
    }

    public void setMinvalueexclusive(boolean minValueExclusive) {
        this.minValueExclusive = minValueExclusive;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }


}