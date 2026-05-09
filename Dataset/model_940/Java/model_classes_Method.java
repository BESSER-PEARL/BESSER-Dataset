





import java.util.List;
import java.util.ArrayList;

public class model_classes_Method extends UnicaseModelElement {

    private String label;
    private String scope;
    private String visibility;
    private boolean stubbed;
    private String properties;
    private String returnType;
    private String signature;



    public model_classes_Method(
        String label,        String scope,        String visibility,        boolean stubbed,        String properties,        String returnType,        String signature    ) {
        super(
        );
        this.label = label;
        this.scope = scope;
        this.visibility = visibility;
        this.stubbed = stubbed;
        this.properties = properties;
        this.returnType = returnType;
        this.signature = signature;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStubbed() {
        return stubbed;
    }

    public void setStubbed(boolean stubbed) {
        this.stubbed = stubbed;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}