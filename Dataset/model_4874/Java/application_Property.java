





import java.util.List;
import java.util.ArrayList;

public class application_Property  {

    private String hidden;
    private String possibleValues;
    private String helpText;
    private String Key;
    private String required;
    private String propertyType;
    private String Value;
    private String changeable;



    public application_Property(
        String hidden,        String possibleValues,        String helpText,        String Key,        String required,        String propertyType,        String Value,        String changeable    ) {
        this.hidden = hidden;
        this.possibleValues = possibleValues;
        this.helpText = helpText;
        this.Key = Key;
        this.required = required;
        this.propertyType = propertyType;
        this.Value = Value;
        this.changeable = changeable;
    }


    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getPossiblevalues() {
        return possibleValues;
    }

    public void setPossiblevalues(String possibleValues) {
        this.possibleValues = possibleValues;
    }
    public String getHelptext() {
        return helpText;
    }

    public void setHelptext(String helpText) {
        this.helpText = helpText;
    }
    public String getKey() {
        return Key;
    }

    public void setKey(String Key) {
        this.Key = Key;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }


}