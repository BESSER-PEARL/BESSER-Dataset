





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_FeatureDiagram extends FeatureElement {

    private boolean graphTypeTree;



    public featureDiagram_FeatureDiagram(
        boolean graphTypeTree    ) {
        super(
        );
        this.graphTypeTree = graphTypeTree;
    }


    public boolean getGraphtypetree() {
        return graphTypeTree;
    }

    public void setGraphtypetree(boolean graphTypeTree) {
        this.graphTypeTree = graphTypeTree;
    }


}