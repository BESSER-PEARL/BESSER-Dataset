





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_CreateDeleteOperation extends AbstractOperation {

    private boolean delete;





    private List<operations_EObjectToModelElementIdMap> operations_eobjecttomodelelementidmaps;




    private List<operations_ReferenceOperation> operations_referenceoperations;


    public esmodel_operations_CreateDeleteOperation(
        boolean delete    ) {
        super(
        );
        this.delete = delete;
        this.operations_eobjecttomodelelementidmaps = new ArrayList<>();
        this.operations_referenceoperations = new ArrayList<>();
    }

    public esmodel_operations_CreateDeleteOperation(
        boolean delete        ArrayList<operations_EObjectToModelElementIdMap> operations_eobjecttomodelelementidmaps,        ArrayList<operations_ReferenceOperation> operations_referenceoperations    ) {
        this.delete = delete;
        this.operations_eobjecttomodelelementidmaps = operations_eobjecttomodelelementidmaps;
        this.operations_referenceoperations = operations_referenceoperations;
    }

    public boolean getDelete() {
        return delete;
    }

    public void setDelete(boolean delete) {
        this.delete = delete;
    }

    public List<operations_EObjectToModelElementIdMap> getOperations_eobjecttomodelelementidmaps() {
        return operations_eobjecttomodelelementidmaps;
    }

    public void addOperations_eobjecttomodelelementidmap(Operations_eobjecttomodelelementidmap operations_eobjecttomodelelementidmap) {
        this.operations_eobjecttomodelelementidmaps.add(operations_eobjecttomodelelementidmap);
    }
    public List<operations_ReferenceOperation> getOperations_referenceoperations() {
        return operations_referenceoperations;
    }

    public void addOperations_referenceoperation(Operations_referenceoperation operations_referenceoperation) {
        this.operations_referenceoperations.add(operations_referenceoperation);
    }

}