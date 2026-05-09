





import java.util.List;
import java.util.ArrayList;

public class model_classes_Attribute extends UnicaseModelElement {

    private String label;
    private String visibility;
    private String signature;
    private String properties;
    private String defaultValue;
    private String scope;
    private String type;



    public model_classes_Attribute(
        String label,        String visibility,        String signature,        String properties,        String defaultValue,        String scope,        String type    ) {
        super(
        );
        this.label = label;
        this.visibility = visibility;
        this.signature = signature;
        this.properties = properties;
        this.defaultValue = defaultValue;
        this.scope = scope;
        this.type = type;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}