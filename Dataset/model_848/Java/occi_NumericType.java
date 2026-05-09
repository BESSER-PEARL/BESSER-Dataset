





import java.util.List;
import java.util.ArrayList;

public class occi_NumericType extends BasicType {

    private String maxInclusive;
    private String minInclusive;
    private String type;
    private String maxExclusive;
    private String totalDigits;
    private String minExclusive;



    public occi_NumericType(
        String maxInclusive,        String minInclusive,        String type,        String maxExclusive,        String totalDigits,        String minExclusive    ) {
        super(
        );
        this.maxInclusive = maxInclusive;
        this.minInclusive = minInclusive;
        this.type = type;
        this.maxExclusive = maxExclusive;
        this.totalDigits = totalDigits;
        this.minExclusive = minExclusive;
    }


    public String getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(String maxInclusive) {
        this.maxInclusive = maxInclusive;
    }
    public String getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(String minInclusive) {
        this.minInclusive = minInclusive;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMaxexclusive() {
        return maxExclusive;
    }

    public void setMaxexclusive(String maxExclusive) {
        this.maxExclusive = maxExclusive;
    }
    public String getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(String totalDigits) {
        this.totalDigits = totalDigits;
    }
    public String getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(String minExclusive) {
        this.minExclusive = minExclusive;
    }


}