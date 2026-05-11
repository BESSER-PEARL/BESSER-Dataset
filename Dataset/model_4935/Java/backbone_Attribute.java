





import java.util.List;
import java.util.ArrayList;

public class backbone_Attribute extends NamedElement {

    private String cardinality;
    private String defaultValue;



    public backbone_Attribute(
        String cardinality,        String defaultValue    ) {
        super(
        );
        this.cardinality = cardinality;
        this.defaultValue = defaultValue;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}