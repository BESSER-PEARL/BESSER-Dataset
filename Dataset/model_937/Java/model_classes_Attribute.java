





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String signature;
    private String scope;
    private String properties;
    private String visibility;
    private String defaultValue;
    private String label;
    private String type;



    public model_classes_Attribute(
        String signature,        String scope,        String properties,        String visibility,        String defaultValue,        String label,        String type    ) {
        super(
        );
        this.signature = signature;
        this.scope = scope;
        this.properties = properties;
        this.visibility = visibility;
        this.defaultValue = defaultValue;
        this.label = label;
        this.type = type;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}