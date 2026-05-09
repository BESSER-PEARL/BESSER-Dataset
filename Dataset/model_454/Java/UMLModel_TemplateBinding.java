





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TemplateBinding extends DirectedRelationship {

    private String signature;
    private String boundElement;



    public UMLModel_TemplateBinding(
        String signature,        String boundElement    ) {
        super(
        );
        this.signature = signature;
        this.boundElement = boundElement;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getBoundelement() {
        return boundElement;
    }

    public void setBoundelement(String boundElement) {
        this.boundElement = boundElement;
    }


}