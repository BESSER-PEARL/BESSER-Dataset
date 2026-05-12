





import java.util.List;
import java.util.ArrayList;

public class model_HasLabel  {






    private List<model_Label> model_labels;




    private model_Label model_label;


    public model_HasLabel(
    ) {
        this.model_labels = new ArrayList<>();
    }

    public model_HasLabel(
        ArrayList<model_Label> model_labels    ) {
        this.model_labels = model_labels;
    }


    public List<model_Label> getModel_labels() {
        return model_labels;
    }

    public void addModel_label(Model_label model_label) {
        this.model_labels.add(model_label);
    }
    public model_Label getModel_label() {
        return model_label;
    }

    public void setModel_label(model_Label model_label) {
        this.model_label = model_label;
    }

}