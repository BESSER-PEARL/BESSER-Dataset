





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String visibility;
    private String defaultValue;
    private String label;
    private String scope;
    private String type;
    private String properties;
    private String signature;



    public model_classes_Attribute(
        String visibility,        String defaultValue,        String label,        String scope,        String type,        String properties,        String signature    ) {
        super(
        );
        this.visibility = visibility;
        this.defaultValue = defaultValue;
        this.label = label;
        this.scope = scope;
        this.type = type;
        this.properties = properties;
        this.signature = signature;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}