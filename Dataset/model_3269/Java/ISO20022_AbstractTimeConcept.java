





import java.util.List;
import java.util.ArrayList;

public class ISO20022_AbstractTimeConcept extends DataType {

    private String pattern;
    private String minExclusive;
    private String minInclusive;
    private String maxInclusive;
    private String maxExclusive;



    public ISO20022_AbstractTimeConcept(
        String pattern,        String minExclusive,        String minInclusive,        String maxInclusive,        String maxExclusive    ) {
        super(
        );
        this.pattern = pattern;
        this.minExclusive = minExclusive;
        this.minInclusive = minInclusive;
        this.maxInclusive = maxInclusive;
        this.maxExclusive = maxExclusive;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(String minExclusive) {
        this.minExclusive = minExclusive;
    }
    public String getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(String minInclusive) {
        this.minInclusive = minInclusive;
    }
    public String getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(String maxInclusive) {
        this.maxInclusive = maxInclusive;
    }
    public String getMaxexclusive() {
        return maxExclusive;
    }

    public void setMaxexclusive(String maxExclusive) {
        this.maxExclusive = maxExclusive;
    }


}