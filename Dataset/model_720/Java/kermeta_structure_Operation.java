





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Operation extends MultiplicityElement {

    private String isAbstract;





    private structure_Operation structure_operation;


    public kermeta_structure_Operation(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public structure_Operation getStructure_operation() {
        return structure_operation;
    }

    public void setStructure_operation(structure_Operation structure_operation) {
        this.structure_operation = structure_operation;
    }

}