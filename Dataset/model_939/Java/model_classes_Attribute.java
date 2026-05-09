





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String defaultValue;
    private String visibility;
    private String signature;
    private String type;
    private String label;
    private String scope;
    private String properties;



    public model_classes_Attribute(
        String defaultValue,        String visibility,        String signature,        String type,        String label,        String scope,        String properties    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.visibility = visibility;
        this.signature = signature;
        this.type = type;
        this.label = label;
        this.scope = scope;
        this.properties = properties;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }


}