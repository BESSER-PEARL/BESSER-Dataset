





import java.util.List;
import java.util.ArrayList;

public class model2_R  {






    private List<model2_A> model2_as;


    public model2_R(
    ) {
        this.model2_as = new ArrayList<>();
    }

    public model2_R(
        ArrayList<model2_A> model2_as    ) {
        this.model2_as = model2_as;
    }


    public List<model2_A> getModel2_as() {
        return model2_as;
    }

    public void addModel2_a(Model2_a model2_a) {
        this.model2_as.add(model2_a);
    }

}