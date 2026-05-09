





import java.util.List;
import java.util.ArrayList;

public class Wires_DecisionNode extends WiresElement {

    private String expression;





    private List<Wires_InputActualParameter> wires_inputactualparameters;




    private Wires_Transformation wires_transformation;




    private List<Wires_Transformation> wires_transformations;




    private List<Wires_Transformation> wires_transformations;


    public Wires_DecisionNode(
        String expression    ) {
        super(
        );
        this.expression = expression;
        this.wires_inputactualparameters = new ArrayList<>();
        this.wires_transformations = new ArrayList<>();
        this.wires_transformations = new ArrayList<>();
    }

    public Wires_DecisionNode(
        String expression        ArrayList<Wires_InputActualParameter> wires_inputactualparameters,        ArrayList<Wires_Transformation> wires_transformations,        ArrayList<Wires_Transformation> wires_transformations    ) {
        this.expression = expression;
        this.wires_inputactualparameters = wires_inputactualparameters;
        this.wires_transformations = wires_transformations;
        this.wires_transformations = wires_transformations;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public List<Wires_InputActualParameter> getWires_inputactualparameters() {
        return wires_inputactualparameters;
    }

    public void addWires_inputactualparameter(Wires_inputactualparameter wires_inputactualparameter) {
        this.wires_inputactualparameters.add(wires_inputactualparameter);
    }
    public Wires_Transformation getWires_transformation() {
        return wires_transformation;
    }

    public void setWires_transformation(Wires_Transformation wires_transformation) {
        this.wires_transformation = wires_transformation;
    }
    public List<Wires_Transformation> getWires_transformations() {
        return wires_transformations;
    }

    public void addWires_transformation(Wires_transformation wires_transformation) {
        this.wires_transformations.add(wires_transformation);
    }
    public List<Wires_Transformation> getWires_transformations() {
        return wires_transformations;
    }

    public void addWires_transformation(Wires_transformation wires_transformation) {
        this.wires_transformations.add(wires_transformation);
    }

}