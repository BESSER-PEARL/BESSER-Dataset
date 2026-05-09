





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_CompositeOperation extends AbstractOperation {

    private String compositeDescription;
    private String compositeName;
    private boolean reversed;





    private List<operations_AbstractOperation> operations_abstractoperations;




    private operations_AbstractOperation operations_abstractoperation;


    public esmodel_operations_CompositeOperation(
        String compositeDescription,        String compositeName,        boolean reversed    ) {
        super(
        );
        this.compositeDescription = compositeDescription;
        this.compositeName = compositeName;
        this.reversed = reversed;
        this.operations_abstractoperations = new ArrayList<>();
    }

    public esmodel_operations_CompositeOperation(
        String compositeDescription,        String compositeName,        boolean reversed        ArrayList<operations_AbstractOperation> operations_abstractoperations    ) {
        this.compositeDescription = compositeDescription;
        this.compositeName = compositeName;
        this.reversed = reversed;
        this.operations_abstractoperations = operations_abstractoperations;
    }

    public String getCompositedescription() {
        return compositeDescription;
    }

    public void setCompositedescription(String compositeDescription) {
        this.compositeDescription = compositeDescription;
    }
    public String getCompositename() {
        return compositeName;
    }

    public void setCompositename(String compositeName) {
        this.compositeName = compositeName;
    }
    public boolean getReversed() {
        return reversed;
    }

    public void setReversed(boolean reversed) {
        this.reversed = reversed;
    }

    public List<operations_AbstractOperation> getOperations_abstractoperations() {
        return operations_abstractoperations;
    }

    public void addOperations_abstractoperation(Operations_abstractoperation operations_abstractoperation) {
        this.operations_abstractoperations.add(operations_abstractoperation);
    }
    public operations_AbstractOperation getOperations_abstractoperation() {
        return operations_abstractoperation;
    }

    public void setOperations_abstractoperation(operations_AbstractOperation operations_abstractoperation) {
        this.operations_abstractoperation = operations_abstractoperation;
    }

}