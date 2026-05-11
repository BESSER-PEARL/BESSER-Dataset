





import java.util.List;
import java.util.ArrayList;

public class website_DataType extends Classifier {

    private String validationPattern;
    private String placeholder;
    private String interfaceType;
    private String persistentType;
    private String ormType;





    private website_FilterParameter website_filterparameter;


    public website_DataType(
        String validationPattern,        String placeholder,        String interfaceType,        String persistentType,        String ormType    ) {
        super(
        );
        this.validationPattern = validationPattern;
        this.placeholder = placeholder;
        this.interfaceType = interfaceType;
        this.persistentType = persistentType;
        this.ormType = ormType;
    }


    public String getValidationpattern() {
        return validationPattern;
    }

    public void setValidationpattern(String validationPattern) {
        this.validationPattern = validationPattern;
    }
    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public String getPersistenttype() {
        return persistentType;
    }

    public void setPersistenttype(String persistentType) {
        this.persistentType = persistentType;
    }
    public String getOrmtype() {
        return ormType;
    }

    public void setOrmtype(String ormType) {
        this.ormType = ormType;
    }

    public website_FilterParameter getWebsite_filterparameter() {
        return website_filterparameter;
    }

    public void setWebsite_filterparameter(website_FilterParameter website_filterparameter) {
        this.website_filterparameter = website_filterparameter;
    }

}