





import java.util.List;
import java.util.ArrayList;

public class org_structure_OperationAdaptationOperator extends AdaptationOperator {

    private String body;





    private structure_Operation structure_operation;


    public org_structure_OperationAdaptationOperator(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public structure_Operation getStructure_operation() {
        return structure_operation;
    }

    public void setStructure_operation(structure_Operation structure_operation) {
        this.structure_operation = structure_operation;
    }

}