





import java.util.List;
import java.util.ArrayList;

public class model_StackContainer extends Container {






    private List<model_Primitive> model_primitives;


    public model_StackContainer(
    ) {
        super(
        );
        this.model_primitives = new ArrayList<>();
    }

    public model_StackContainer(
        ArrayList<model_Primitive> model_primitives    ) {
        this.model_primitives = model_primitives;
    }


    public List<model_Primitive> getModel_primitives() {
        return model_primitives;
    }

    public void addModel_primitive(Model_primitive model_primitive) {
        this.model_primitives.add(model_primitive);
    }

}