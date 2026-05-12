





import java.util.List;
import java.util.ArrayList;

public class model_Site extends NamedElement, DescribedElement {






    private List<model_TaskSet> model_tasksets;


    public model_Site(
    ) {
        super(
        );
        this.model_tasksets = new ArrayList<>();
    }

    public model_Site(
        ArrayList<model_TaskSet> model_tasksets    ) {
        this.model_tasksets = model_tasksets;
    }


    public List<model_TaskSet> getModel_tasksets() {
        return model_tasksets;
    }

    public void addModel_taskset(Model_taskset model_taskset) {
        this.model_tasksets.add(model_taskset);
    }

}