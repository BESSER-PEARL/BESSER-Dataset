





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String visibility;
    private String type;
    private String defaultValue;
    private String scope;
    private String properties;
    private String label;
    private String signature;



    public model_classes_Attribute(
        String visibility,        String type,        String defaultValue,        String scope,        String properties,        String label,        String signature    ) {
        super(
        );
        this.visibility = visibility;
        this.type = type;
        this.defaultValue = defaultValue;
        this.scope = scope;
        this.properties = properties;
        this.label = label;
        this.signature = signature;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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


}