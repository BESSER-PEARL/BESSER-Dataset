





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String scope;
    private String type;
    private String visibility;
    private String properties;
    private String label;
    private String signature;
    private String defaultValue;



    public model_classes_Attribute(
        String scope,        String type,        String visibility,        String properties,        String label,        String signature,        String defaultValue    ) {
        super(
        );
        this.scope = scope;
        this.type = type;
        this.visibility = visibility;
        this.properties = properties;
        this.label = label;
        this.signature = signature;
        this.defaultValue = defaultValue;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}