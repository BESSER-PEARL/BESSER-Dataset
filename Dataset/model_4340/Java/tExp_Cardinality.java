





import java.util.List;
import java.util.ArrayList;

public class tExp_Cardinality extends Constraint {

    private int minCardinality;
    private int maxCardinality;



    public tExp_Cardinality(
        int minCardinality,        int maxCardinality    ) {
        super(
        );
        this.minCardinality = minCardinality;
        this.maxCardinality = maxCardinality;
    }


    public int getMincardinality() {
        return minCardinality;
    }

    public void setMincardinality(int minCardinality) {
        this.minCardinality = minCardinality;
    }
    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }


}