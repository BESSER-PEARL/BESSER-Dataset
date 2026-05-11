





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Association extends RefAssociation {

    private int minCardinality;
    private int maxCardinality;
    private boolean isAggregation;
    private String name;



    public class_diagramm_Association(
        int minCardinality,        int maxCardinality,        boolean isAggregation,        String name    ) {
        super(
        );
        this.minCardinality = minCardinality;
        this.maxCardinality = maxCardinality;
        this.isAggregation = isAggregation;
        this.name = name;
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
    public boolean getIsaggregation() {
        return isAggregation;
    }

    public void setIsaggregation(boolean isAggregation) {
        this.isAggregation = isAggregation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}