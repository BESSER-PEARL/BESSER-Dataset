





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Feature extends FeatureElement {

    private String name;
    private boolean selected;





    private List<featureDiagram_Operator> featurediagram_operators;




    private featureDiagram_Operator featurediagram_operator;




    private featureDiagram_FeatureDiagram featurediagram_featurediagram;




    private List<featureDiagram_Operator> featurediagram_operators;




    private featureDiagram_FeatureDiagram featurediagram_featurediagram;




    private featureDiagram_Operator featurediagram_operator;




    private featureDiagram_FeatureDiagram featurediagram_featurediagram;


    public featureDiagram_Feature(
        String name,        boolean selected    ) {
        super(
        );
        this.name = name;
        this.selected = selected;
        this.featurediagram_operators = new ArrayList<>();
        this.featurediagram_operators = new ArrayList<>();
    }

    public featureDiagram_Feature(
        String name,        boolean selected        ArrayList<featureDiagram_Operator> featurediagram_operators,        ArrayList<featureDiagram_Operator> featurediagram_operators    ) {
        this.name = name;
        this.selected = selected;
        this.featurediagram_operators = featurediagram_operators;
        this.featurediagram_operators = featurediagram_operators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public List<featureDiagram_Operator> getFeaturediagram_operators() {
        return featurediagram_operators;
    }

    public void addFeaturediagram_operator(Featurediagram_operator featurediagram_operator) {
        this.featurediagram_operators.add(featurediagram_operator);
    }
    public featureDiagram_Operator getFeaturediagram_operator() {
        return featurediagram_operator;
    }

    public void setFeaturediagram_operator(featureDiagram_Operator featurediagram_operator) {
        this.featurediagram_operator = featurediagram_operator;
    }
    public featureDiagram_FeatureDiagram getFeaturediagram_featurediagram() {
        return featurediagram_featurediagram;
    }

    public void setFeaturediagram_featurediagram(featureDiagram_FeatureDiagram featurediagram_featurediagram) {
        this.featurediagram_featurediagram = featurediagram_featurediagram;
    }
    public List<featureDiagram_Operator> getFeaturediagram_operators() {
        return featurediagram_operators;
    }

    public void addFeaturediagram_operator(Featurediagram_operator featurediagram_operator) {
        this.featurediagram_operators.add(featurediagram_operator);
    }
    public featureDiagram_FeatureDiagram getFeaturediagram_featurediagram() {
        return featurediagram_featurediagram;
    }

    public void setFeaturediagram_featurediagram(featureDiagram_FeatureDiagram featurediagram_featurediagram) {
        this.featurediagram_featurediagram = featurediagram_featurediagram;
    }
    public featureDiagram_Operator getFeaturediagram_operator() {
        return featurediagram_operator;
    }

    public void setFeaturediagram_operator(featureDiagram_Operator featurediagram_operator) {
        this.featurediagram_operator = featurediagram_operator;
    }
    public featureDiagram_FeatureDiagram getFeaturediagram_featurediagram() {
        return featurediagram_featurediagram;
    }

    public void setFeaturediagram_featurediagram(featureDiagram_FeatureDiagram featurediagram_featurediagram) {
        this.featurediagram_featurediagram = featurediagram_featurediagram;
    }

}