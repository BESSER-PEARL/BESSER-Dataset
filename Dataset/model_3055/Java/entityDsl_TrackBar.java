





import java.util.List;
import java.util.ArrayList;

public class entityDsl_TrackBar extends WinFormControlType {

    private int denominator;
    private int increment;
    private int minimumValue;
    private int maximumValue;
    private String stringValues;
    private int defaultTick;



    public entityDsl_TrackBar(
        int denominator,        int increment,        int minimumValue,        int maximumValue,        String stringValues,        int defaultTick    ) {
        super(
        );
        this.denominator = denominator;
        this.increment = increment;
        this.minimumValue = minimumValue;
        this.maximumValue = maximumValue;
        this.stringValues = stringValues;
        this.defaultTick = defaultTick;
    }


    public int getDenominator() {
        return denominator;
    }

    public void setDenominator(int denominator) {
        this.denominator = denominator;
    }
    public int getIncrement() {
        return increment;
    }

    public void setIncrement(int increment) {
        this.increment = increment;
    }
    public int getMinimumvalue() {
        return minimumValue;
    }

    public void setMinimumvalue(int minimumValue) {
        this.minimumValue = minimumValue;
    }
    public int getMaximumvalue() {
        return maximumValue;
    }

    public void setMaximumvalue(int maximumValue) {
        this.maximumValue = maximumValue;
    }
    public String getStringvalues() {
        return stringValues;
    }

    public void setStringvalues(String stringValues) {
        this.stringValues = stringValues;
    }
    public int getDefaulttick() {
        return defaultTick;
    }

    public void setDefaulttick(int defaultTick) {
        this.defaultTick = defaultTick;
    }


}