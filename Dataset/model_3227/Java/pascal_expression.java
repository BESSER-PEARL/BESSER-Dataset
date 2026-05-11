





import java.util.List;
import java.util.ArrayList;

public class pascal_expression  {

    private String relationaloperator;





    private pascal_variableDeclaration pascal_variabledeclaration;




    private pascal_expression pascal_expression;


    public pascal_expression(
        String relationaloperator    ) {
        this.relationaloperator = relationaloperator;
    }


    public String getRelationaloperator() {
        return relationaloperator;
    }

    public void setRelationaloperator(String relationaloperator) {
        this.relationaloperator = relationaloperator;
    }

    public pascal_variableDeclaration getPascal_variabledeclaration() {
        return pascal_variabledeclaration;
    }

    public void setPascal_variabledeclaration(pascal_variableDeclaration pascal_variabledeclaration) {
        this.pascal_variabledeclaration = pascal_variabledeclaration;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }

}