





import java.util.List;
import java.util.ArrayList;

public class fmpl_VarDeclaration extends Expression {

    private String name;





    private fmpl_Expression fmpl_expression;


    public fmpl_VarDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fmpl_Expression getFmpl_expression() {
        return fmpl_expression;
    }

    public void setFmpl_expression(fmpl_Expression fmpl_expression) {
        this.fmpl_expression = fmpl_expression;
    }

}