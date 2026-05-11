





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Card extends Operator {

    private int min;
    private int max;



    public featureDiagram_Card(
        int min,        int max    ) {
        super(
        );
        this.min = min;
        this.max = max;
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


}