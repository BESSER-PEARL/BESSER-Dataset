





import java.util.List;
import java.util.ArrayList;

public class amethyst_MemberAccessExpression extends Expression {






    private amethyst_Expression amethyst_expression;




    private amethyst_Symbol amethyst_symbol;


    public amethyst_MemberAccessExpression(
    ) {
        super(
        );
    }



    public amethyst_Expression getAmethyst_expression() {
        return amethyst_expression;
    }

    public void setAmethyst_expression(amethyst_Expression amethyst_expression) {
        this.amethyst_expression = amethyst_expression;
    }
    public amethyst_Symbol getAmethyst_symbol() {
        return amethyst_symbol;
    }

    public void setAmethyst_symbol(amethyst_Symbol amethyst_symbol) {
        this.amethyst_symbol = amethyst_symbol;
    }

}