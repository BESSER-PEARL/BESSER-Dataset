





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_AttributeType extends AttributeEvaluationType {

    private None operator;





    private mutatorenvironment_AttributeScalar mutatorenvironment_attributescalar;


    public mutatorenvironment_AttributeType(
        None operator    ) {
        super(
        );
        this.operator = operator;
    }


    public None getOperator() {
        return operator;
    }

    public void setOperator(None operator) {
        this.operator = operator;
    }

    public mutatorenvironment_AttributeScalar getMutatorenvironment_attributescalar() {
        return mutatorenvironment_attributescalar;
    }

    public void setMutatorenvironment_attributescalar(mutatorenvironment_AttributeScalar mutatorenvironment_attributescalar) {
        this.mutatorenvironment_attributescalar = mutatorenvironment_attributescalar;
    }

}