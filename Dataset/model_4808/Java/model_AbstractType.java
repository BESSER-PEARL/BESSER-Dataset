





import java.util.List;
import java.util.ArrayList;

public class model_AbstractType  {

    private String name;





    private List<model_AbstractType> model_abstracttypes;




    private model_Container model_container;


    public model_AbstractType(
        String name    ) {
        this.name = name;
        this.model_abstracttypes = new ArrayList<>();
    }

    public model_AbstractType(
        String name        ArrayList<model_AbstractType> model_abstracttypes    ) {
        this.name = name;
        this.model_abstracttypes = model_abstracttypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<model_AbstractType> getModel_abstracttypes() {
        return model_abstracttypes;
    }

    public void addModel_abstracttype(Model_abstracttype model_abstracttype) {
        this.model_abstracttypes.add(model_abstracttype);
    }
    public model_Container getModel_container() {
        return model_container;
    }

    public void setModel_container(model_Container model_container) {
        this.model_container = model_container;
    }

}