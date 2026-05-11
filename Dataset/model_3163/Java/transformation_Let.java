





import java.util.List;
import java.util.ArrayList;

public class transformation_Let extends Expression {






    private List<transformation_VariableInitialization> transformation_variableinitializations;




    private transformation_Expression transformation_expression;


    public transformation_Let(
    ) {
        super(
        );
        this.transformation_variableinitializations = new ArrayList<>();
    }

    public transformation_Let(
        ArrayList<transformation_VariableInitialization> transformation_variableinitializations    ) {
        this.transformation_variableinitializations = transformation_variableinitializations;
    }


    public List<transformation_VariableInitialization> getTransformation_variableinitializations() {
        return transformation_variableinitializations;
    }

    public void addTransformation_variableinitialization(Transformation_variableinitialization transformation_variableinitialization) {
        this.transformation_variableinitializations.add(transformation_variableinitialization);
    }
    public transformation_Expression getTransformation_expression() {
        return transformation_expression;
    }

    public void setTransformation_expression(transformation_Expression transformation_expression) {
        this.transformation_expression = transformation_expression;
    }

}