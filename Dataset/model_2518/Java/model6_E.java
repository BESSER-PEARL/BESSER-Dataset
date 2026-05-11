





import java.util.List;
import java.util.ArrayList;

public class model6_E  {






    private List<model6_A> model6_as;


    public model6_E(
    ) {
        this.model6_as = new ArrayList<>();
    }

    public model6_E(
        ArrayList<model6_A> model6_as    ) {
        this.model6_as = model6_as;
    }


    public List<model6_A> getModel6_as() {
        return model6_as;
    }

    public void addModel6_a(Model6_a model6_a) {
        this.model6_as.add(model6_a);
    }

}