





import java.util.List;
import java.util.ArrayList;

public class umm_Content extends BDTProperty {

    private int minExclusive;
    private int totalDigits;
    private int maxInclusive;
    private int minInclusive;
    private int fractionalDigits;
    private int maxExclusive;



    public umm_Content(
        int minExclusive,        int totalDigits,        int maxInclusive,        int minInclusive,        int fractionalDigits,        int maxExclusive    ) {
        super(
        );
        this.minExclusive = minExclusive;
        this.totalDigits = totalDigits;
        this.maxInclusive = maxInclusive;
        this.minInclusive = minInclusive;
        this.fractionalDigits = fractionalDigits;
        this.maxExclusive = maxExclusive;
    }


    public int getMinexclusive() {
        return minExclusive;
    }

    public void setMinexclusive(int minExclusive) {
        this.minExclusive = minExclusive;
    }
    public int getTotaldigits() {
        return totalDigits;
    }

    public void setTotaldigits(int totalDigits) {
        this.totalDigits = totalDigits;
    }
    public int getMaxinclusive() {
        return maxInclusive;
    }

    public void setMaxinclusive(int maxInclusive) {
        this.maxInclusive = maxInclusive;
    }
    public int getMininclusive() {
        return minInclusive;
    }

    public void setMininclusive(int minInclusive) {
        this.minInclusive = minInclusive;
    }
    public int getFractionaldigits() {
        return fractionalDigits;
    }

    public void setFractionaldigits(int fractionalDigits) {
        this.fractionalDigits = fractionalDigits;
    }
    public int getMaxexclusive() {
        return maxExclusive;
    }

    public void setMaxexclusive(int maxExclusive) {
        this.maxExclusive = maxExclusive;
    }


}