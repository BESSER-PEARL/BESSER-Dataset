





import java.util.List;
import java.util.ArrayList;

public class model_classes_Method extends UnicaseModelElement {

    private String scope;
    private String visibility;
    private String label;
    private String properties;
    private String returnType;
    private boolean stubbed;
    private String signature;



    public model_classes_Method(
        String scope,        String visibility,        String label,        String properties,        String returnType,        boolean stubbed,        String signature    ) {
        super(
        );
        this.scope = scope;
        this.visibility = visibility;
        this.label = label;
        this.properties = properties;
        this.returnType = returnType;
        this.stubbed = stubbed;
        this.signature = signature;
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
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public boolean getStubbed() {
        return stubbed;
    }

    public void setStubbed(boolean stubbed) {
        this.stubbed = stubbed;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}