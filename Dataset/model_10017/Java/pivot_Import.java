





import java.util.List;
import java.util.ArrayList;

public class pivot_Import extends NamedElement {






    private pivot_Model pivot_model;




    private pivot_Namespace pivot_namespace;


    public pivot_Import(
    ) {
        super(
        );
    }



    public pivot_Model getPivot_model() {
        return pivot_model;
    }

    public void setPivot_model(pivot_Model pivot_model) {
        this.pivot_model = pivot_model;
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }

}