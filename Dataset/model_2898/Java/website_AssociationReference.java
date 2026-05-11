





import java.util.List;
import java.util.ArrayList;

public class website_AssociationReference  {

    private String name;





    private website_Label website_label;




    private website_Association website_association;


    public website_AssociationReference(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public website_Label getWebsite_label() {
        return website_label;
    }

    public void setWebsite_label(website_Label website_label) {
        this.website_label = website_label;
    }
    public website_Association getWebsite_association() {
        return website_association;
    }

    public void setWebsite_association(website_Association website_association) {
        this.website_association = website_association;
    }

}