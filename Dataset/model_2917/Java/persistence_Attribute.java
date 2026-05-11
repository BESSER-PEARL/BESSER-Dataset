





import java.util.List;
import java.util.ArrayList;

public class persistence_Attribute extends Feature, Label {

    private String validationPattern;
    private String placeholder;
    private String inputClass;





    private persistence_EntityOrView persistence_entityorview;


    public persistence_Attribute(
        String validationPattern,        String placeholder,        String inputClass    ) {
        super(
        );
        this.validationPattern = validationPattern;
        this.placeholder = placeholder;
        this.inputClass = inputClass;
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
    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }

    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }

}