





import java.util.List;
import java.util.ArrayList;

public class persistence_EncapsulatedAttribute extends Attribute, EncapsulatedFeature {

    private String cardinality;
    private String name;





    private persistence_Attribute persistence_attribute;


    public persistence_EncapsulatedAttribute(
        String cardinality,        String name    ) {
        super(
        );
        this.cardinality = cardinality;
        this.name = name;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public persistence_Attribute getPersistence_attribute() {
        return persistence_attribute;
    }

    public void setPersistence_attribute(persistence_Attribute persistence_attribute) {
        this.persistence_attribute = persistence_attribute;
    }

}