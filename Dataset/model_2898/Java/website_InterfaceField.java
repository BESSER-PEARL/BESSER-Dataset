





import java.util.List;
import java.util.ArrayList;

public class website_InterfaceField extends UnitField, NamedDisplayElement {

    private String placeholder;
    private String validationPattern;
    private boolean required;
    private String inputClass;
    private String defaultValue;



    public website_InterfaceField(
        String placeholder,        String validationPattern,        boolean required,        String inputClass,        String defaultValue    ) {
        super(
        );
        this.placeholder = placeholder;
        this.validationPattern = validationPattern;
        this.required = required;
        this.inputClass = inputClass;
        this.defaultValue = defaultValue;
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
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}