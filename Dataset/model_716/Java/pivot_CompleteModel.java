





import java.util.List;
import java.util.ArrayList;

public class pivot_CompleteModel extends NamedElement {






    private pivot_OrphanCompletePackage pivot_orphancompletepackage;




    private pivot_PrimitiveCompletePackage pivot_primitivecompletepackage;


    public pivot_CompleteModel(
    ) {
        super(
        );
    }



    public pivot_OrphanCompletePackage getPivot_orphancompletepackage() {
        return pivot_orphancompletepackage;
    }

    public void setPivot_orphancompletepackage(pivot_OrphanCompletePackage pivot_orphancompletepackage) {
        this.pivot_orphancompletepackage = pivot_orphancompletepackage;
    }
    public pivot_PrimitiveCompletePackage getPivot_primitivecompletepackage() {
        return pivot_primitivecompletepackage;
    }

    public void setPivot_primitivecompletepackage(pivot_PrimitiveCompletePackage pivot_primitivecompletepackage) {
        this.pivot_primitivecompletepackage = pivot_primitivecompletepackage;
    }

}