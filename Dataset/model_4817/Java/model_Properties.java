





import java.util.List;
import java.util.ArrayList;

public class model_Properties  {






    private List<model_Property> model_propertys;


    public model_Properties(
    ) {
        this.model_propertys = new ArrayList<>();
    }

    public model_Properties(
        ArrayList<model_Property> model_propertys    ) {
        this.model_propertys = model_propertys;
    }


    public List<model_Property> getModel_propertys() {
        return model_propertys;
    }

    public void addModel_property(Model_property model_property) {
        this.model_propertys.add(model_property);
    }

}