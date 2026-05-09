





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_OperationCS extends CSTNode {






    private TypeCS typecs;




    private SimpleNameCS simplenamecs;


    public ocl_cst_OperationCS(
    ) {
        super(
        );
    }



    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }
    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }

}