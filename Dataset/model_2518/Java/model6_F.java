





import java.util.List;
import java.util.ArrayList;

public class model6_F  {






    private List<model6_E> model6_es;


    public model6_F(
    ) {
        this.model6_es = new ArrayList<>();
    }

    public model6_F(
        ArrayList<model6_E> model6_es    ) {
        this.model6_es = model6_es;
    }


    public List<model6_E> getModel6_es() {
        return model6_es;
    }

    public void addModel6_e(Model6_e model6_e) {
        this.model6_es.add(model6_e);
    }

}