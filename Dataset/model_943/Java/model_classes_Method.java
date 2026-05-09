





import java.util.List;
import java.util.ArrayList;

public class model_classes_Method extends UnicaseModelElement {

    private String properties;
    private String scope;
    private String returnType;
    private String label;
    private boolean stubbed;
    private String signature;
    private String visibility;



    public model_classes_Method(
        String properties,        String scope,        String returnType,        String label,        boolean stubbed,        String signature,        String visibility    ) {
        super(
        );
        this.properties = properties;
        this.scope = scope;
        this.returnType = returnType;
        this.label = label;
        this.stubbed = stubbed;
        this.signature = signature;
        this.visibility = visibility;
    }


    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}