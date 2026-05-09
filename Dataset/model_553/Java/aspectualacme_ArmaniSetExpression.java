





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniSetExpression extends ArmaniPrimitiveExpression {

    private String referenceType;
    private String reference;



    public aspectualacme_ArmaniSetExpression(
        String referenceType,        String reference    ) {
        super(
        );
        this.referenceType = referenceType;
        this.reference = reference;
    }


    public String getReferencetype() {
        return referenceType;
    }

    public void setReferencetype(String referenceType) {
        this.referenceType = referenceType;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}