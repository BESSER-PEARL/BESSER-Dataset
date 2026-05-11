





import java.util.List;
import java.util.ArrayList;

public class di_LabeledEdge extends Edge {






    private List<di_Label> di_labels;


    public di_LabeledEdge(
    ) {
        super(
        );
        this.di_labels = new ArrayList<>();
    }

    public di_LabeledEdge(
        ArrayList<di_Label> di_labels    ) {
        this.di_labels = di_labels;
    }


    public List<di_Label> getDi_labels() {
        return di_labels;
    }

    public void addDi_label(Di_label di_label) {
        this.di_labels.add(di_label);
    }

}