





import java.util.List;
import java.util.ArrayList;

public class ocl_constraints_OclConstraintsModel extends LocatedElement {

    private String metamodel;
    private String name;



    public ocl_constraints_OclConstraintsModel(
        String metamodel,        String name    ) {
        super(
        );
        this.metamodel = metamodel;
        this.name = name;
    }


    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}