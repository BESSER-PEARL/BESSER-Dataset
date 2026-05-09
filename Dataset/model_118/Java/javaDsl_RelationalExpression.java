





import java.util.List;
import java.util.ArrayList;

public class javaDsl_RelationalExpression  {

    private String classes;
    private String operators;





    private javaDsl_EqualityExpression javadsl_equalityexpression;


    public javaDsl_RelationalExpression(
        String classes,        String operators    ) {
        this.classes = classes;
        this.operators = operators;
    }


    public String getClasses() {
        return classes;
    }

    public void setClasses(String classes) {
        this.classes = classes;
    }
    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public javaDsl_EqualityExpression getJavadsl_equalityexpression() {
        return javadsl_equalityexpression;
    }

    public void setJavadsl_equalityexpression(javaDsl_EqualityExpression javadsl_equalityexpression) {
        this.javadsl_equalityexpression = javadsl_equalityexpression;
    }

}