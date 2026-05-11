





import java.util.List;
import java.util.ArrayList;

public class transformation_Lambda extends Expression {






    private List<transformation_VariableDefinition> transformation_variabledefinitions;




    private transformation_Expression transformation_expression;


    public transformation_Lambda(
    ) {
        super(
        );
        this.transformation_variabledefinitions = new ArrayList<>();
    }

    public transformation_Lambda(
        ArrayList<transformation_VariableDefinition> transformation_variabledefinitions    ) {
        this.transformation_variabledefinitions = transformation_variabledefinitions;
    }


    public List<transformation_VariableDefinition> getTransformation_variabledefinitions() {
        return transformation_variabledefinitions;
    }

    public void addTransformation_variabledefinition(Transformation_variabledefinition transformation_variabledefinition) {
        this.transformation_variabledefinitions.add(transformation_variabledefinition);
    }
    public transformation_Expression getTransformation_expression() {
        return transformation_expression;
    }

    public void setTransformation_expression(transformation_Expression transformation_expression) {
        this.transformation_expression = transformation_expression;
    }

}