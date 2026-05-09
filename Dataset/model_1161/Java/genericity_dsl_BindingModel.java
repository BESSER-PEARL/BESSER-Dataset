





import java.util.List;
import java.util.ArrayList;

public class genericity_dsl_BindingModel extends LocatedElement {

    private String name;
    private String metamodel;



    public genericity_dsl_BindingModel(
        String name,        String metamodel    ) {
        super(
        );
        this.name = name;
        this.metamodel = metamodel;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }


}