





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_Variable extends SymbolicDeclaration {






    private logiclanguage_AggregatedParameterSubstitution logiclanguage_aggregatedparametersubstitution;




    private logiclanguage_FunctionDefinition logiclanguage_functiondefinition;




    private logiclanguage_RelationDefinition logiclanguage_relationdefinition;




    private logiclanguage_AggregateExpression logiclanguage_aggregateexpression;


    public logiclanguage_Variable(
    ) {
        super(
        );
    }



    public logiclanguage_AggregatedParameterSubstitution getLogiclanguage_aggregatedparametersubstitution() {
        return logiclanguage_aggregatedparametersubstitution;
    }

    public void setLogiclanguage_aggregatedparametersubstitution(logiclanguage_AggregatedParameterSubstitution logiclanguage_aggregatedparametersubstitution) {
        this.logiclanguage_aggregatedparametersubstitution = logiclanguage_aggregatedparametersubstitution;
    }
    public logiclanguage_FunctionDefinition getLogiclanguage_functiondefinition() {
        return logiclanguage_functiondefinition;
    }

    public void setLogiclanguage_functiondefinition(logiclanguage_FunctionDefinition logiclanguage_functiondefinition) {
        this.logiclanguage_functiondefinition = logiclanguage_functiondefinition;
    }
    public logiclanguage_RelationDefinition getLogiclanguage_relationdefinition() {
        return logiclanguage_relationdefinition;
    }

    public void setLogiclanguage_relationdefinition(logiclanguage_RelationDefinition logiclanguage_relationdefinition) {
        this.logiclanguage_relationdefinition = logiclanguage_relationdefinition;
    }
    public logiclanguage_AggregateExpression getLogiclanguage_aggregateexpression() {
        return logiclanguage_aggregateexpression;
    }

    public void setLogiclanguage_aggregateexpression(logiclanguage_AggregateExpression logiclanguage_aggregateexpression) {
        this.logiclanguage_aggregateexpression = logiclanguage_aggregateexpression;
    }

}