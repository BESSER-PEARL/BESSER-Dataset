





import java.util.List;
import java.util.ArrayList;

public class pivot_CompleteModel extends NamedElement {






    private List<pivot_Model> pivot_models;


    public pivot_CompleteModel(
    ) {
        super(
        );
        this.pivot_models = new ArrayList<>();
    }

    public pivot_CompleteModel(
        ArrayList<pivot_Model> pivot_models    ) {
        this.pivot_models = pivot_models;
    }


    public List<pivot_Model> getPivot_models() {
        return pivot_models;
    }

    public void addPivot_model(Pivot_model pivot_model) {
        this.pivot_models.add(pivot_model);
    }

}