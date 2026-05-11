





import java.util.List;
import java.util.ArrayList;

public class eol_expression_NameExpression extends Expression {

    private boolean isType;
    private String name;





    private eol_expression_VariableDeclarationExpression eol_expression_variabledeclarationexpression;


    public eol_expression_NameExpression(
        boolean isType,        String name    ) {
        super(
        );
        this.isType = isType;
        this.name = name;
    }


    public boolean getIstype() {
        return isType;
    }

    public void setIstype(boolean isType) {
        this.isType = isType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eol_expression_VariableDeclarationExpression getEol_expression_variabledeclarationexpression() {
        return eol_expression_variabledeclarationexpression;
    }

    public void setEol_expression_variabledeclarationexpression(eol_expression_VariableDeclarationExpression eol_expression_variabledeclarationexpression) {
        this.eol_expression_variabledeclarationexpression = eol_expression_variabledeclarationexpression;
    }

}