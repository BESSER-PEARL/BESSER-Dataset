





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_QuantificationExpression extends expressions_Expression, declarations_VariableContainer {

    private String quantifier;



    public uppaal_expressions_QuantificationExpression(
        String quantifier    ) {
        super(
        );
        this.quantifier = quantifier;
    }


    public String getQuantifier() {
        return quantifier;
    }

    public void setQuantifier(String quantifier) {
        this.quantifier = quantifier;
    }


}