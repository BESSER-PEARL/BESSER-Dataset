





import java.util.List;
import java.util.ArrayList;

public class iso20022_Decimal extends DataType {

    private String minExclusive;
    private String maxInclusive;
    private String maxExclusive;
    private String pattern;
    private String totalDigits;
    private String minInclusive;
    private String fractionDigits;



    public iso20022_Decimal(
        String minExclusive,        String maxInclusive,        String maxExclusive,        String pattern,        String totalDigits,        String minInclusive,        String fractionDigits    ) {
        super(
        );
        this.minExclusive = minExclusive;
        this.maxInclusive = maxInclusive;
        this.maxExclusive = maxExclusive;
        this.pattern = pattern;
        this.totalDigits = totalDigits;
        this.minInclusive = minInclusive;
        this.fractionDigits = fractionDigits;
    }


    public String getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(String minExclusive) {
        this.minExclusive = minExclusive;
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
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(String totalDigits) {
        this.totalDigits = totalDigits;
    }
    public String getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(String minInclusive) {
        this.minInclusive = minInclusive;
    }
    public String getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(String fractionDigits) {
        this.fractionDigits = fractionDigits;
    }


}