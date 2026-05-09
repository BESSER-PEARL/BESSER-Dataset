





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_OperationCS extends CSTNode {






    private SimpleNameCS simplenamecs;




    private TypeCS typecs;


    public ocl_cst_OperationCS(
    ) {
        super(
        );
    }



    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }
    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }

}