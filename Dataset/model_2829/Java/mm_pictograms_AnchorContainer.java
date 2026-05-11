





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_AnchorContainer extends PictogramElement {






    private List<Anchor> anchors;


    public mm_pictograms_AnchorContainer(
    ) {
        super(
        );
        this.anchors = new ArrayList<>();
    }

    public mm_pictograms_AnchorContainer(
        ArrayList<Anchor> anchors    ) {
        this.anchors = anchors;
    }


    public List<Anchor> getAnchors() {
        return anchors;
    }

    public void addAnchor(Anchor anchor) {
        this.anchors.add(anchor);
    }

}