





import java.util.List;
import java.util.ArrayList;

public class application_Property  {

    private String propertyType;
    private String required;
    private String helpText;
    private String changeable;
    private String Key;
    private String possibleValues;
    private String Value;
    private String hidden;





    private application_Configuration application_configuration;


    public application_Property(
        String propertyType,        String required,        String helpText,        String changeable,        String Key,        String possibleValues,        String Value,        String hidden    ) {
        this.propertyType = propertyType;
        this.required = required;
        this.helpText = helpText;
        this.changeable = changeable;
        this.Key = Key;
        this.possibleValues = possibleValues;
        this.Value = Value;
        this.hidden = hidden;
    }


    public String getPropertytype() {
        return propertyType;
    }

    public void setPropertytype(String propertyType) {
        this.propertyType = propertyType;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getHelptext() {
        return helpText;
    }

    public void setHelptext(String helpText) {
        this.helpText = helpText;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
    }
    public String getPossiblevalues() {
        return possibleValues;
    }

    public void setPossiblevalues(String possibleValues) {
        this.possibleValues = possibleValues;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }

    public application_Configuration getApplication_configuration() {
        return application_configuration;
    }

    public void setApplication_configuration(application_Configuration application_configuration) {
        this.application_configuration = application_configuration;
    }

}