





import java.util.List;
import java.util.ArrayList;

public class website_UnitElement extends UnitFeature {

    private String validationPattern;
    private boolean obfuscateFormFields;
    private String placeholder;
    private String name;





    private website_Expression website_expression;




    private website_Attribute website_attribute;


    public website_UnitElement(
        String validationPattern,        boolean obfuscateFormFields,        String placeholder,        String name    ) {
        super(
        );
        this.validationPattern = validationPattern;
        this.obfuscateFormFields = obfuscateFormFields;
        this.placeholder = placeholder;
        this.name = name;
    }


    public String getValidationpattern() {
        return validationPattern;
    }

    public void setValidationpattern(String validationPattern) {
        this.validationPattern = validationPattern;
    }
    public boolean getObfuscateformfields() {
        return obfuscateFormFields;
    }

    public void setObfuscateformfields(boolean obfuscateFormFields) {
        this.obfuscateFormFields = obfuscateFormFields;
    }
    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public website_Expression getWebsite_expression() {
        return website_expression;
    }

    public void setWebsite_expression(website_Expression website_expression) {
        this.website_expression = website_expression;
    }
    public website_Attribute getWebsite_attribute() {
        return website_attribute;
    }

    public void setWebsite_attribute(website_Attribute website_attribute) {
        this.website_attribute = website_attribute;
    }

}