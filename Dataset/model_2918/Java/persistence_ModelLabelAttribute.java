





import java.util.List;
import java.util.ArrayList;

public class persistence_ModelLabelAttribute extends ModelLabelFeature {

    private String dateFormat;





    private persistence_Attribute persistence_attribute;


    public persistence_ModelLabelAttribute(
        String dateFormat    ) {
        super(
        );
        this.dateFormat = dateFormat;
    }


    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }

    public persistence_Attribute getPersistence_attribute() {
        return persistence_attribute;
    }

    public void setPersistence_attribute(persistence_Attribute persistence_attribute) {
        this.persistence_attribute = persistence_attribute;
    }

}