





import java.util.List;
import java.util.ArrayList;

public class vcml_NumericType extends CharacteristicType {

    private boolean intervalValuesAllowed;
    private String unit;
    private boolean negativeValuesAllowed;
    private int decimalPlaces;



    public vcml_NumericType(
        boolean intervalValuesAllowed,        String unit,        boolean negativeValuesAllowed,        int decimalPlaces    ) {
        super(
        );
        this.intervalValuesAllowed = intervalValuesAllowed;
        this.unit = unit;
        this.negativeValuesAllowed = negativeValuesAllowed;
        this.decimalPlaces = decimalPlaces;
    }


    public boolean getIntervalvaluesallowed() {
        return intervalValuesAllowed;
    }

    public void setIntervalvaluesallowed(boolean intervalValuesAllowed) {
        this.intervalValuesAllowed = intervalValuesAllowed;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public boolean getNegativevaluesallowed() {
        return negativeValuesAllowed;
    }

    public void setNegativevaluesallowed(boolean negativeValuesAllowed) {
        this.negativeValuesAllowed = negativeValuesAllowed;
    }
    public int getDecimalplaces() {
        return decimalPlaces;
    }

    public void setDecimalplaces(int decimalPlaces) {
        this.decimalPlaces = decimalPlaces;
    }


}