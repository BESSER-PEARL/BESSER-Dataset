





import java.util.List;
import java.util.ArrayList;

public class datastyle_ScientificNumberType  {

    private String decimalPlaces;
    private String grouping;
    private String minIntegerDigits;
    private String minExponentDigits;



    public datastyle_ScientificNumberType(
        String decimalPlaces,        String grouping,        String minIntegerDigits,        String minExponentDigits    ) {
        this.decimalPlaces = decimalPlaces;
        this.grouping = grouping;
        this.minIntegerDigits = minIntegerDigits;
        this.minExponentDigits = minExponentDigits;
    }


    public String getDecimalplaces() {
        return decimalPlaces;
    }

    public void setDecimalplaces(String decimalPlaces) {
        this.decimalPlaces = decimalPlaces;
    }
    public String getGrouping() {
        return grouping;
    }

    public void setGrouping(String grouping) {
        this.grouping = grouping;
    }
    public String getMinintegerdigits() {
        return minIntegerDigits;
    }

    public void setMinintegerdigits(String minIntegerDigits) {
        this.minIntegerDigits = minIntegerDigits;
    }
    public String getMinexponentdigits() {
        return minExponentDigits;
    }

    public void setMinexponentdigits(String minExponentDigits) {
        this.minExponentDigits = minExponentDigits;
    }


}