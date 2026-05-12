





import java.util.List;
import java.util.ArrayList;

public class PNML_LabeledElement extends LocatedElement {






    private List<Label> labels;


    public PNML_LabeledElement(
    ) {
        super(
        );
        this.labels = new ArrayList<>();
    }

    public PNML_LabeledElement(
        ArrayList<Label> labels    ) {
        this.labels = labels;
    }


    public List<Label> getLabels() {
        return labels;
    }

    public void addLabel(Label label) {
        this.labels.add(label);
    }

}