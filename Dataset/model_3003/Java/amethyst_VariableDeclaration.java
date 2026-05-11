





import java.util.List;
import java.util.ArrayList;

public class amethyst_VariableDeclaration extends Symbol {






    private amethyst_Expression amethyst_expression;




    private amethyst_AbstractType amethyst_abstracttype;


    public amethyst_VariableDeclaration(
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
    public amethyst_AbstractType getAmethyst_abstracttype() {
        return amethyst_abstracttype;
    }

    public void setAmethyst_abstracttype(amethyst_AbstractType amethyst_abstracttype) {
        this.amethyst_abstracttype = amethyst_abstracttype;
    }

}