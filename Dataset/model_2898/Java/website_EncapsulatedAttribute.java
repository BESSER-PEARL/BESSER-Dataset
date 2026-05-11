





import java.util.List;
import java.util.ArrayList;

public class website_EncapsulatedAttribute extends Attribute, EncapsulatedFeature {

    private String cardinality;
    private String name;





    private website_Attribute website_attribute;


    public website_EncapsulatedAttribute(
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

    public website_Attribute getWebsite_attribute() {
        return website_attribute;
    }

    public void setWebsite_attribute(website_Attribute website_attribute) {
        this.website_attribute = website_attribute;
    }

}