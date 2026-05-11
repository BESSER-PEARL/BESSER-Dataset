





import java.util.List;
import java.util.ArrayList;

public class website_ModelLabelAttribute extends ModelLabelFeature {

    private String dateFormat;





    private website_Attribute website_attribute;


    public website_ModelLabelAttribute(
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

    public website_Attribute getWebsite_attribute() {
        return website_attribute;
    }

    public void setWebsite_attribute(website_Attribute website_attribute) {
        this.website_attribute = website_attribute;
    }

}