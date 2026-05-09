





import java.util.List;
import java.util.ArrayList;

public class model_classes_Method extends UnicaseModelElement {

    private String label;
    private String visibility;
    private String scope;
    private boolean stubbed;
    private String signature;
    private String returnType;
    private String properties;



    public model_classes_Method(
        String label,        String visibility,        String scope,        boolean stubbed,        String signature,        String returnType,        String properties    ) {
        super(
        );
        this.label = label;
        this.visibility = visibility;
        this.scope = scope;
        this.stubbed = stubbed;
        this.signature = signature;
        this.returnType = returnType;
        this.properties = properties;
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
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
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
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }


}