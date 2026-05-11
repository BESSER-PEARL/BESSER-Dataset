





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_FeatureDiagram extends FeatureElement {

    private boolean graphTypeTree;





    private featureDiagram_Feature featurediagram_feature;




    private List<featureDiagram_ConstraintEdge> featurediagram_constraintedges;




    private List<featureDiagram_Feature> featurediagram_features;




    private featureDiagram_Feature featurediagram_feature;


    public featureDiagram_FeatureDiagram(
        boolean graphTypeTree    ) {
        super(
        );
        this.graphTypeTree = graphTypeTree;
        this.featurediagram_constraintedges = new ArrayList<>();
        this.featurediagram_features = new ArrayList<>();
    }

    public featureDiagram_FeatureDiagram(
        boolean graphTypeTree        ArrayList<featureDiagram_ConstraintEdge> featurediagram_constraintedges,        ArrayList<featureDiagram_Feature> featurediagram_features    ) {
        this.graphTypeTree = graphTypeTree;
        this.featurediagram_constraintedges = featurediagram_constraintedges;
        this.featurediagram_features = featurediagram_features;
    }

    public boolean getGraphtypetree() {
        return graphTypeTree;
    }

    public void setGraphtypetree(boolean graphTypeTree) {
        this.graphTypeTree = graphTypeTree;
    }

    public featureDiagram_Feature getFeaturediagram_feature() {
        return featurediagram_feature;
    }

    public void setFeaturediagram_feature(featureDiagram_Feature featurediagram_feature) {
        this.featurediagram_feature = featurediagram_feature;
    }
    public List<featureDiagram_ConstraintEdge> getFeaturediagram_constraintedges() {
        return featurediagram_constraintedges;
    }

    public void addFeaturediagram_constraintedge(Featurediagram_constraintedge featurediagram_constraintedge) {
        this.featurediagram_constraintedges.add(featurediagram_constraintedge);
    }
    public List<featureDiagram_Feature> getFeaturediagram_features() {
        return featurediagram_features;
    }

    public void addFeaturediagram_feature(Featurediagram_feature featurediagram_feature) {
        this.featurediagram_features.add(featurediagram_feature);
    }
    public featureDiagram_Feature getFeaturediagram_feature() {
        return featurediagram_feature;
    }

    public void setFeaturediagram_feature(featureDiagram_Feature featurediagram_feature) {
        this.featurediagram_feature = featurediagram_feature;
    }

}