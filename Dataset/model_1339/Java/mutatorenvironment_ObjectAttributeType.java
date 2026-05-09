





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_ObjectAttributeType extends AttributeEvaluationType {

    private None operator;





    private mutatorenvironment_ObjectEmitter mutatorenvironment_objectemitter;


    public mutatorenvironment_ObjectAttributeType(
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

    public mutatorenvironment_ObjectEmitter getMutatorenvironment_objectemitter() {
        return mutatorenvironment_objectemitter;
    }

    public void setMutatorenvironment_objectemitter(mutatorenvironment_ObjectEmitter mutatorenvironment_objectemitter) {
        this.mutatorenvironment_objectemitter = mutatorenvironment_objectemitter;
    }

}