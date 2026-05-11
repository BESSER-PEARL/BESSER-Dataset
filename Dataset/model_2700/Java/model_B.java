





import java.util.List;
import java.util.ArrayList;

public class model_B  {






    private model_A model_a;




    private List<model_A> model_as;


    public model_B(
    ) {
        this.model_as = new ArrayList<>();
    }

    public model_B(
        ArrayList<model_A> model_as    ) {
        this.model_as = model_as;
    }


    public model_A getModel_a() {
        return model_a;
    }

    public void setModel_a(model_A model_a) {
        this.model_a = model_a;
    }
    public List<model_A> getModel_as() {
        return model_as;
    }

    public void addModel_a(Model_a model_a) {
        this.model_as.add(model_a);
    }

}