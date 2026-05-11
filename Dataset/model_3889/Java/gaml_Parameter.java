





import java.util.List;
import java.util.ArrayList;

public class gaml_Parameter extends Expression {

    private String builtInFacetKey;





    private gaml_Expression gaml_expression;




    private gaml_VariableRef gaml_variableref;


    public gaml_Parameter(
        String builtInFacetKey    ) {
        super(
        );
        this.builtInFacetKey = builtInFacetKey;
    }


    public String getBuiltinfacetkey() {
        return builtInFacetKey;
    }

    public void setBuiltinfacetkey(String builtInFacetKey) {
        this.builtInFacetKey = builtInFacetKey;
    }

    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }
    public gaml_VariableRef getGaml_variableref() {
        return gaml_variableref;
    }

    public void setGaml_variableref(gaml_VariableRef gaml_variableref) {
        this.gaml_variableref = gaml_variableref;
    }

}