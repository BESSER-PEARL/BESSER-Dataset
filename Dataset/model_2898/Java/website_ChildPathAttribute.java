





import java.util.List;
import java.util.ArrayList;

public class website_ChildPathAttribute extends ChildPath {

    private String name;





    private website_Attribute website_attribute;


    public website_ChildPathAttribute(
        String name    ) {
        super(
        );
        this.name = name;
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