





import java.util.List;
import java.util.ArrayList;

public class datastyle_FractionType  {

    private String denominatorValue;
    private String grouping;
    private String minDenominatorDigits;
    private String minNumeratorDigits;
    private String minIntegerDigits;



    public datastyle_FractionType(
        String denominatorValue,        String grouping,        String minDenominatorDigits,        String minNumeratorDigits,        String minIntegerDigits    ) {
        this.denominatorValue = denominatorValue;
        this.grouping = grouping;
        this.minDenominatorDigits = minDenominatorDigits;
        this.minNumeratorDigits = minNumeratorDigits;
        this.minIntegerDigits = minIntegerDigits;
    }


    public String getDenominatorvalue() {
        return denominatorValue;
    }

    public void setDenominatorvalue(String denominatorValue) {
        this.denominatorValue = denominatorValue;
    }
    public String getGrouping() {
        return grouping;
    }

    public void setGrouping(String grouping) {
        this.grouping = grouping;
    }
    public String getMindenominatordigits() {
        return minDenominatorDigits;
    }

    public void setMindenominatordigits(String minDenominatorDigits) {
        this.minDenominatorDigits = minDenominatorDigits;
    }
    public String getMinnumeratordigits() {
        return minNumeratorDigits;
    }

    public void setMinnumeratordigits(String minNumeratorDigits) {
        this.minNumeratorDigits = minNumeratorDigits;
    }
    public String getMinintegerdigits() {
        return minIntegerDigits;
    }

    public void setMinintegerdigits(String minIntegerDigits) {
        this.minIntegerDigits = minIntegerDigits;
    }


}