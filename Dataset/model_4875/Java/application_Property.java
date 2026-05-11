





import java.util.List;
import java.util.ArrayList;

public class application_Property  {

    private String Value;
    private String possibleValues;
    private String required;
    private String Key;
    private String helpText;
    private String propertyType;
    private String hidden;
    private String changeable;





    private application_Configuration application_configuration;


    public application_Property(
        String Value,        String possibleValues,        String required,        String Key,        String helpText,        String propertyType,        String hidden,        String changeable    ) {
        this.Value = Value;
        this.possibleValues = possibleValues;
        this.required = required;
        this.Key = Key;
        this.helpText = helpText;
        this.propertyType = propertyType;
        this.hidden = hidden;
        this.changeable = changeable;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getPossiblevalues() {
        return possibleValues;
    }

    public void setPossiblevalues(String possibleValues) {
        this.possibleValues = possibleValues;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public String getHelptext() {
        return helpText;
    }

    public void setHelptext(String helpText) {
        this.helpText = helpText;
    }
    public String getPropertytype() {
        return propertyType;
    }

    public void setPropertytype(String propertyType) {
        this.propertyType = propertyType;
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