





import java.util.List;
import java.util.ArrayList;

public class sml_IntegerRanges extends AbstractRanges {

    private int min;
    private int max;
    private int values;



    public sml_IntegerRanges(
        int min,        int max,        int values    ) {
        super(
        );
        this.min = min;
        this.max = max;
        this.values = values;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getValues() {
        return values;
    }

    public void setValues(int values) {
        this.values = values;
    }


}