





import java.util.List;
import java.util.ArrayList;

public class gaml_ExpressionList extends Expression {






    private gaml_Parameters gaml_parameters;




    private gaml_Access gaml_access;




    private List<gaml_Expression> gaml_expressions;




    private gaml_Array gaml_array;


    public gaml_ExpressionList(
    ) {
        super(
        );
        this.gaml_expressions = new ArrayList<>();
    }

    public gaml_ExpressionList(
        ArrayList<gaml_Expression> gaml_expressions    ) {
        this.gaml_expressions = gaml_expressions;
    }


    public gaml_Parameters getGaml_parameters() {
        return gaml_parameters;
    }

    public void setGaml_parameters(gaml_Parameters gaml_parameters) {
        this.gaml_parameters = gaml_parameters;
    }
    public gaml_Access getGaml_access() {
        return gaml_access;
    }

    public void setGaml_access(gaml_Access gaml_access) {
        this.gaml_access = gaml_access;
    }
    public List<gaml_Expression> getGaml_expressions() {
        return gaml_expressions;
    }

    public void addGaml_expression(Gaml_expression gaml_expression) {
        this.gaml_expressions.add(gaml_expression);
    }
    public gaml_Array getGaml_array() {
        return gaml_array;
    }

    public void setGaml_array(gaml_Array gaml_array) {
        this.gaml_array = gaml_array;
    }

}