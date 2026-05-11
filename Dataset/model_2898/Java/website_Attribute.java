





import java.util.List;
import java.util.ArrayList;

public class website_Attribute extends Feature, Label {

    private String placeholder;
    private String validationPattern;
    private String inputClass;





    private website_Authentication website_authentication;




    private website_EntityOrView website_entityorview;


    public website_Attribute(
        String placeholder,        String validationPattern,        String inputClass    ) {
        super(
        );
        this.placeholder = placeholder;
        this.validationPattern = validationPattern;
        this.inputClass = inputClass;
    }


    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }
    public String getValidationpattern() {
        return validationPattern;
    }

    public void setValidationpattern(String validationPattern) {
        this.validationPattern = validationPattern;
    }
    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }

    public website_Authentication getWebsite_authentication() {
        return website_authentication;
    }

    public void setWebsite_authentication(website_Authentication website_authentication) {
        this.website_authentication = website_authentication;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }

}