





import java.util.List;
import java.util.ArrayList;

public class datastyle_NumberType  {

    private String decimalReplacement;
    private String grouping;
    private String displayFactor;
    private String minIntegerDigits;
    private String decimalPlaces;



    public datastyle_NumberType(
        String decimalReplacement,        String grouping,        String displayFactor,        String minIntegerDigits,        String decimalPlaces    ) {
        this.decimalReplacement = decimalReplacement;
        this.grouping = grouping;
        this.displayFactor = displayFactor;
        this.minIntegerDigits = minIntegerDigits;
        this.decimalPlaces = decimalPlaces;
    }


    public String getDecimalreplacement() {
        return decimalReplacement;
    }

    public void setDecimalreplacement(String decimalReplacement) {
        this.decimalReplacement = decimalReplacement;
    }
    public String getGrouping() {
        return grouping;
    }

    public void setGrouping(String grouping) {
        this.grouping = grouping;
    }
    public String getDisplayfactor() {
        return displayFactor;
    }

    public void setDisplayfactor(String displayFactor) {
        this.displayFactor = displayFactor;
    }
    public String getMinintegerdigits() {
        return minIntegerDigits;
    }

    public void setMinintegerdigits(String minIntegerDigits) {
        this.minIntegerDigits = minIntegerDigits;
    }
    public String getDecimalplaces() {
        return decimalPlaces;
    }

    public void setDecimalplaces(String decimalPlaces) {
        this.decimalPlaces = decimalPlaces;
    }


}