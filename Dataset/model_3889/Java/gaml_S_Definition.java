





import java.util.List;
import java.util.ArrayList;

public class gaml_S_Definition extends ActionDefinition, S_Declaration {






    private gaml_Expression gaml_expression;


    public gaml_S_Definition(
    ) {
        super(
        );
    }



    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }

}