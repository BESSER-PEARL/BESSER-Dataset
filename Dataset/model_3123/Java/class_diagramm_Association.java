





import java.util.List;
import java.util.ArrayList;

public class class_diagramm_Association extends RefAssociation {

    private int maxCardinality;
    private int minCardinality;
    private String name;
    private boolean isAggregation;





    private class_diagramm_RefClass class_diagramm_refclass;




    private class_diagramm_RefClass class_diagramm_refclass;


    public class_diagramm_Association(
        int maxCardinality,        int minCardinality,        String name,        boolean isAggregation    ) {
        super(
        );
        this.maxCardinality = maxCardinality;
        this.minCardinality = minCardinality;
        this.name = name;
        this.isAggregation = isAggregation;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsaggregation() {
        return isAggregation;
    }

    public void setIsaggregation(boolean isAggregation) {
        this.isAggregation = isAggregation;
    }

    public class_diagramm_RefClass getClass_diagramm_refclass() {
        return class_diagramm_refclass;
    }

    public void setClass_diagramm_refclass(class_diagramm_RefClass class_diagramm_refclass) {
        this.class_diagramm_refclass = class_diagramm_refclass;
    }
    public class_diagramm_RefClass getClass_diagramm_refclass() {
        return class_diagramm_refclass;
    }

    public void setClass_diagramm_refclass(class_diagramm_RefClass class_diagramm_refclass) {
        this.class_diagramm_refclass = class_diagramm_refclass;
    }

}