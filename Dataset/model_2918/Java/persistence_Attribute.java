





import java.util.List;
import java.util.ArrayList;

public class persistence_Attribute extends Label, Feature {

    private String inputClass;
    private String validationPattern;





    private persistence_EntityOrView persistence_entityorview;


    public persistence_Attribute(
        String inputClass,        String validationPattern    ) {
        super(
        );
        this.inputClass = inputClass;
        this.validationPattern = validationPattern;
    }


    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }
    public String getValidationpattern() {
        return validationPattern;
    }

    public void setValidationpattern(String validationPattern) {
        this.validationPattern = validationPattern;
    }

    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }

}