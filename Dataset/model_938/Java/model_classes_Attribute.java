





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String label;
    private String properties;
    private String visibility;
    private String signature;
    private String defaultValue;
    private String type;
    private String scope;



    public model_classes_Attribute(
        String label,        String properties,        String visibility,        String signature,        String defaultValue,        String type,        String scope    ) {
        super(
        );
        this.label = label;
        this.properties = properties;
        this.visibility = visibility;
        this.signature = signature;
        this.defaultValue = defaultValue;
        this.type = type;
        this.scope = scope;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}