





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Action extends ExecutableNode {

    private String context;
    private String output;
    private String input;





    private List<UMLModel_Constraint> umlmodel_constraints;




    private List<UMLModel_Constraint> umlmodel_constraints;


    public UMLModel_Action(
        String context,        String output,        String input    ) {
        super(
        );
        this.context = context;
        this.output = output;
        this.input = input;
        this.umlmodel_constraints = new ArrayList<>();
        this.umlmodel_constraints = new ArrayList<>();
    }

    public UMLModel_Action(
        String context,        String output,        String input        ArrayList<UMLModel_Constraint> umlmodel_constraints,        ArrayList<UMLModel_Constraint> umlmodel_constraints    ) {
        this.context = context;
        this.output = output;
        this.input = input;
        this.umlmodel_constraints = umlmodel_constraints;
        this.umlmodel_constraints = umlmodel_constraints;
    }

    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public List<UMLModel_Constraint> getUmlmodel_constraints() {
        return umlmodel_constraints;
    }

    public void addUmlmodel_constraint(Umlmodel_constraint umlmodel_constraint) {
        this.umlmodel_constraints.add(umlmodel_constraint);
    }
    public List<UMLModel_Constraint> getUmlmodel_constraints() {
        return umlmodel_constraints;
    }

    public void addUmlmodel_constraint(Umlmodel_constraint umlmodel_constraint) {
        this.umlmodel_constraints.add(umlmodel_constraint);
    }

}