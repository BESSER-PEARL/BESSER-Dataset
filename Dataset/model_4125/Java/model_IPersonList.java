





import java.util.List;
import java.util.ArrayList;

public class model_IPersonList  {






    private List<model_IPerson> model_ipersons;


    public model_IPersonList(
    ) {
        this.model_ipersons = new ArrayList<>();
    }

    public model_IPersonList(
        ArrayList<model_IPerson> model_ipersons    ) {
        this.model_ipersons = model_ipersons;
    }


    public List<model_IPerson> getModel_ipersons() {
        return model_ipersons;
    }

    public void addModel_iperson(Model_iperson model_iperson) {
        this.model_ipersons.add(model_iperson);
    }

}