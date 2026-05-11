





import java.util.List;
import java.util.ArrayList;

public class application_Property  {

    private String Value;
    private String helpText;
    private String required;
    private String propertyType;
    private String possibleValues;
    private String Key;
    private String hidden;
    private String changeable;





    private application_Configuration application_configuration;


    public application_Property(
        String Value,        String helpText,        String required,        String propertyType,        String possibleValues,        String Key,        String hidden,        String changeable    ) {
        this.Value = Value;
        this.helpText = helpText;
        this.required = required;
        this.propertyType = propertyType;
        this.possibleValues = possibleValues;
        this.Key = Key;
        this.hidden = hidden;
        this.changeable = changeable;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getHelptext() {
        return helpText;
    }

    public void setHelptext(String helpText) {
        this.helpText = helpText;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getPropertytype() {
        return propertyType;
    }

    public void setPropertytype(String propertyType) {
        this.propertyType = propertyType;
    }
    public String getPossiblevalues() {
        return possibleValues;
    }

    public void setPossiblevalues(String possibleValues) {
        this.possibleValues = possibleValues;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }

    public application_Configuration getApplication_configuration() {
        return application_configuration;
    }

    public void setApplication_configuration(application_Configuration application_configuration) {
        this.application_configuration = application_configuration;
    }

}