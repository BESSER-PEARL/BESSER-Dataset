





import java.util.List;
import java.util.ArrayList;

public class iso20022_AbstractDateTimeConcept extends DataType {

    private String minInclusive;
    private String pattern;
    private String maxInclusive;
    private String maxExclusive;
    private String minExclusive;



    public iso20022_AbstractDateTimeConcept(
        String minInclusive,        String pattern,        String maxInclusive,        String maxExclusive,        String minExclusive    ) {
        super(
        );
        this.minInclusive = minInclusive;
        this.pattern = pattern;
        this.maxInclusive = maxInclusive;
        this.maxExclusive = maxExclusive;
        this.minExclusive = minExclusive;
    }


    public String getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(String minInclusive) {
        this.minInclusive = minInclusive;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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
    public String getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(String minExclusive) {
        this.minExclusive = minExclusive;
    }


}