





import java.util.List;
import java.util.ArrayList;

public class sxfm_CardinalizedElement  {

    private int maxCardinality;
    private int minCardinality;



    public sxfm_CardinalizedElement(
        int maxCardinality,        int minCardinality    ) {
        this.maxCardinality = maxCardinality;
        this.minCardinality = minCardinality;
    }


    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }
    public int getMincardinality() {
        return minCardinality;
    }

    public void setMincardinality(int minCardinality) {
        this.minCardinality = minCardinality;
    }


}