





import java.util.List;
import java.util.ArrayList;

public class gaml_ExpressionList extends Expression {






    private gaml_Array gaml_array;




    private List<gaml_Expression> gaml_expressions;


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


    public gaml_Array getGaml_array() {
        return gaml_array;
    }

    public void setGaml_array(gaml_Array gaml_array) {
        this.gaml_array = gaml_array;
    }
    public List<gaml_Expression> getGaml_expressions() {
        return gaml_expressions;
    }

    public void addGaml_expression(Gaml_expression gaml_expression) {
        this.gaml_expressions.add(gaml_expression);
    }

}