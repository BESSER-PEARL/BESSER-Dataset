





import java.util.List;
import java.util.ArrayList;

public class ISO20022_XSDDecimal extends DataType {

    private String maxExclusive;
    private String fractionDigits;
    private String minInclusive;
    private String pattern;
    private String maxInclusive;
    private String minExclusive;
    private String totalDigits;



    public ISO20022_XSDDecimal(
        String maxExclusive,        String fractionDigits,        String minInclusive,        String pattern,        String maxInclusive,        String minExclusive,        String totalDigits    ) {
        super(
        );
        this.maxExclusive = maxExclusive;
        this.fractionDigits = fractionDigits;
        this.minInclusive = minInclusive;
        this.pattern = pattern;
        this.maxInclusive = maxInclusive;
        this.minExclusive = minExclusive;
        this.totalDigits = totalDigits;
    }


    public String getMaxexclusive() {
        return maxExclusive;
    }

    public void setMaxexclusive(String maxExclusive) {
        this.maxExclusive = maxExclusive;
    }
    public String getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(String fractionDigits) {
        this.fractionDigits = fractionDigits;
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
    public String getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(String minExclusive) {
        this.minExclusive = minExclusive;
    }
    public String getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(String totalDigits) {
        this.totalDigits = totalDigits;
    }


}