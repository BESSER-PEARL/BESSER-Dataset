





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ArrayExpression  {






    private javaDsl_Expression javadsl_expression;




    private javaDsl_ArrayAccess javadsl_arrayaccess;




    private javaDsl_Primary javadsl_primary;


    public javaDsl_ArrayExpression(
    ) {
    }



    public javaDsl_Expression getJavadsl_expression() {
        return javadsl_expression;
    }

    public void setJavadsl_expression(javaDsl_Expression javadsl_expression) {
        this.javadsl_expression = javadsl_expression;
    }
    public javaDsl_ArrayAccess getJavadsl_arrayaccess() {
        return javadsl_arrayaccess;
    }

    public void setJavadsl_arrayaccess(javaDsl_ArrayAccess javadsl_arrayaccess) {
        this.javadsl_arrayaccess = javadsl_arrayaccess;
    }
    public javaDsl_Primary getJavadsl_primary() {
        return javadsl_primary;
    }

    public void setJavadsl_primary(javaDsl_Primary javadsl_primary) {
        this.javadsl_primary = javadsl_primary;
    }

}