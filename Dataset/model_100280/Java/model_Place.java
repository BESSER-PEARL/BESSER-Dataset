





import java.util.List;
import java.util.ArrayList;

public class model_Place extends PlaceNode {






    private List<model_RefPlace> model_refplaces;




    private model_RefPlace model_refplace;


    public model_Place(
    ) {
        super(
        );
        this.model_refplaces = new ArrayList<>();
    }

    public model_Place(
        ArrayList<model_RefPlace> model_refplaces    ) {
        this.model_refplaces = model_refplaces;
    }


    public List<model_RefPlace> getModel_refplaces() {
        return model_refplaces;
    }

    public void addModel_refplace(Model_refplace model_refplace) {
        this.model_refplaces.add(model_refplace);
    }
    public model_RefPlace getModel_refplace() {
        return model_refplace;
    }

    public void setModel_refplace(model_RefPlace model_refplace) {
        this.model_refplace = model_refplace;
    }

}