





import java.util.List;
import java.util.ArrayList;

public class model_LibraryManager  {






    private List<model_GeppettoLibrary> model_geppettolibrarys;


    public model_LibraryManager(
    ) {
        this.model_geppettolibrarys = new ArrayList<>();
    }

    public model_LibraryManager(
        ArrayList<model_GeppettoLibrary> model_geppettolibrarys    ) {
        this.model_geppettolibrarys = model_geppettolibrarys;
    }


    public List<model_GeppettoLibrary> getModel_geppettolibrarys() {
        return model_geppettolibrarys;
    }

    public void addModel_geppettolibrary(Model_geppettolibrary model_geppettolibrary) {
        this.model_geppettolibrarys.add(model_geppettolibrary);
    }

}