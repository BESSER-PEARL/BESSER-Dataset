





import java.util.List;
import java.util.ArrayList;

public class org_structure_UnresolvedOperation extends structure_UnresolvedReference, structure_TypeContainer, structure_AbstractOperation {

    private String operationIdentifier;



    public org_structure_UnresolvedOperation(
        String operationIdentifier    ) {
        super(
        );
        this.operationIdentifier = operationIdentifier;
    }


    public String getOperationidentifier() {
        return operationIdentifier;
    }

    public void setOperationidentifier(String operationIdentifier) {
        this.operationIdentifier = operationIdentifier;
    }


}