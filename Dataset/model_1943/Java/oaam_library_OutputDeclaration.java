





import java.util.List;
import java.util.ArrayList;

public class oaam_library_OutputDeclaration extends OaamBaseElementA {

    private int upperBound;
    private String unit;
    private String postcondition;
    private String range;
    private int lowerBound;



    public oaam_library_OutputDeclaration(
        int upperBound,        String unit,        String postcondition,        String range,        int lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.unit = unit;
        this.postcondition = postcondition;
        this.range = range;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }


}