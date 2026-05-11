





import java.util.List;
import java.util.ArrayList;

public class feature_FeatureTreeNode  {

    private int minCardinality;
    private int maxCardinality;



    public feature_FeatureTreeNode(
        int minCardinality,        int maxCardinality    ) {
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