





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Attribute2Attribute extends mappings_AttributeRightPart, mappings_Feature2Feature {

    private String cardinality;





    private List<AttributeRef> attributerefs;


    public frontend_mappings_Attribute2Attribute(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
        this.attributerefs = new ArrayList<>();
    }

    public frontend_mappings_Attribute2Attribute(
        String cardinality        ArrayList<AttributeRef> attributerefs    ) {
        this.cardinality = cardinality;
        this.attributerefs = attributerefs;
    }

    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public List<AttributeRef> getAttributerefs() {
        return attributerefs;
    }

    public void addAttributeref(Attributeref attributeref) {
        this.attributerefs.add(attributeref);
    }

}