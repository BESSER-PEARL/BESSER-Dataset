





import java.util.List;
import java.util.ArrayList;

public class iso20022_Decimal extends DataType {

    private String maxInclusive;
    private String pattern;
    private String maxExclusive;
    private String minExclusive;
    private String minInclusive;
    private String totalDigits;
    private String fractionDigits;



    public iso20022_Decimal(
        String maxInclusive,        String pattern,        String maxExclusive,        String minExclusive,        String minInclusive,        String totalDigits,        String fractionDigits    ) {
        super(
        );
        this.maxInclusive = maxInclusive;
        this.pattern = pattern;
        this.maxExclusive = maxExclusive;
        this.minExclusive = minExclusive;
        this.minInclusive = minInclusive;
        this.totalDigits = totalDigits;
        this.fractionDigits = fractionDigits;
    }


    public String getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(String maxInclusive) {
        this.maxInclusive = maxInclusive;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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
    public String getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(String minInclusive) {
        this.minInclusive = minInclusive;
    }
    public String getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(String totalDigits) {
        this.totalDigits = totalDigits;
    }
    public String getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(String fractionDigits) {
        this.fractionDigits = fractionDigits;
    }


}