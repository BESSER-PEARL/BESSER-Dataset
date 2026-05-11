





import java.util.List;
import java.util.ArrayList;

public class entityrelationship_Relationship extends Elements_with_Attributes {

    private int order;
    private String type_relationship;
    private String name_relationship;
    private String cardinality;



    public entityrelationship_Relationship(
        int order,        String type_relationship,        String name_relationship,        String cardinality    ) {
        super(
        );
        this.order = order;
        this.type_relationship = type_relationship;
        this.name_relationship = name_relationship;
        this.cardinality = cardinality;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getType_relationship() {
        return type_relationship;
    }

    public void setType_relationship(String type_relationship) {
        this.type_relationship = type_relationship;
    }
    public String getName_relationship() {
        return name_relationship;
    }

    public void setName_relationship(String name_relationship) {
        this.name_relationship = name_relationship;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }


}