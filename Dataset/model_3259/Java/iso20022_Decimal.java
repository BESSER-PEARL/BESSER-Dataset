





import java.util.List;
import java.util.ArrayList;

public class iso20022_Decimal extends DataType {

    private String maxInclusive;
    private String maxExclusive;
    private String fractionDigits;
    private String pattern;
    private String minExclusive;
    private String minInclusive;
    private String totalDigits;



    public iso20022_Decimal(
        String maxInclusive,        String maxExclusive,        String fractionDigits,        String pattern,        String minExclusive,        String minInclusive,        String totalDigits    ) {
        super(
        );
        this.maxInclusive = maxInclusive;
        this.maxExclusive = maxExclusive;
        this.fractionDigits = fractionDigits;
        this.pattern = pattern;
        this.minExclusive = minExclusive;
        this.minInclusive = minInclusive;
        this.totalDigits = totalDigits;
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
    public String getFractiondigits() {
        return fractionDigits;
    }

    public void setFractiondigits(String fractionDigits) {
        this.fractionDigits = fractionDigits;
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
    public String getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(String totalDigits) {
        this.totalDigits = totalDigits;
    }


}