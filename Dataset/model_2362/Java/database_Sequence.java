





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private int maxValue;
    private int minValue;
    private int start;
    private int increment;



    public database_Sequence(
        int maxValue,        int minValue,        int start,        int increment    ) {
        super(
        );
        this.maxValue = maxValue;
        this.minValue = minValue;
        this.start = start;
        this.increment = increment;
    }


    public int getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(int maxValue) {
        this.maxValue = maxValue;
    }
    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getIncrement() {
        return increment;
    }

    public void setIncrement(int increment) {
        this.increment = increment;
    }


}