





import java.util.List;
import java.util.ArrayList;

public class iso20022_AbstractDateTimeConcept extends DataType {

    private String pattern;
    private String minExclusive;
    private String minInclusive;
    private String maxExclusive;
    private String maxInclusive;



    public iso20022_AbstractDateTimeConcept(
        String pattern,        String minExclusive,        String minInclusive,        String maxExclusive,        String maxInclusive    ) {
        super(
        );
        this.pattern = pattern;
        this.minExclusive = minExclusive;
        this.minInclusive = minInclusive;
        this.maxExclusive = maxExclusive;
        this.maxInclusive = maxInclusive;
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
    public String getMaxexclusive() {
        return maxExclusive;
    }

    public void setMaxexclusive(String maxExclusive) {
        this.maxExclusive = maxExclusive;
    }
    public String getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(String maxInclusive) {
        this.maxInclusive = maxInclusive;
    }


}