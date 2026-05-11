





import java.util.List;
import java.util.ArrayList;

public class gast_annotations_Clone extends core_ModelElement, annotations_ModelAnnotation {






    private Root root;




    private List<CloneInstance> cloneinstances;


    public gast_annotations_Clone(
    ) {
        super(
        );
        this.cloneinstances = new ArrayList<>();
    }

    public gast_annotations_Clone(
        ArrayList<CloneInstance> cloneinstances    ) {
        this.cloneinstances = cloneinstances;
    }


    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }
    public List<CloneInstance> getCloneinstances() {
        return cloneinstances;
    }

    public void addCloneinstance(Cloneinstance cloneinstance) {
        this.cloneinstances.add(cloneinstance);
    }

}