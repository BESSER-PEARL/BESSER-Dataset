





import java.util.List;
import java.util.ArrayList;

public class model_From extends AbstractAssignBound, BPELExtensibleElement {

    private String endpointReference;
    private String unsafeLiteral;
    private String literal;
    private String opaque;





    private model_Variable model_variable;




    private model_Copy model_copy;


    public model_From(
        String endpointReference,        String unsafeLiteral,        String literal,        String opaque    ) {
        super(
        );
        this.endpointReference = endpointReference;
        this.unsafeLiteral = unsafeLiteral;
        this.literal = literal;
        this.opaque = opaque;
    }


    public String getEndpointreference() {
        return endpointReference;
    }

    public void setEndpointreference(String endpointReference) {
        this.endpointReference = endpointReference;
    }
    public String getUnsafeliteral() {
        return unsafeLiteral;
    }

    public void setUnsafeliteral(String unsafeLiteral) {
        this.unsafeLiteral = unsafeLiteral;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getOpaque() {
        return opaque;
    }

    public void setOpaque(String opaque) {
        this.opaque = opaque;
    }

    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public model_Copy getModel_copy() {
        return model_copy;
    }

    public void setModel_copy(model_Copy model_copy) {
        this.model_copy = model_copy;
    }

}