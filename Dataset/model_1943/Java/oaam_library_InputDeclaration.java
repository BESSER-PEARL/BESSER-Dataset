





import java.util.List;
import java.util.ArrayList;

public class oaam_library_InputDeclaration extends OaamBaseElementA {

    private int lowerBound;
    private String unit;
    private String precondition;
    private String range;
    private int upperBound;



    public oaam_library_InputDeclaration(
        int lowerBound,        String unit,        String precondition,        String range,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.unit = unit;
        this.precondition = precondition;
        this.range = range;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }


}