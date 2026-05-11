





import java.util.List;
import java.util.ArrayList;

public class javali_VarExpression extends Expression {






    private List<javali_Identifier> javali_identifiers;




    private List<javali_Expression> javali_expressions;




    private javali_VarAssign javali_varassign;


    public javali_VarExpression(
    ) {
        super(
        );
        this.javali_identifiers = new ArrayList<>();
        this.javali_expressions = new ArrayList<>();
    }

    public javali_VarExpression(
        ArrayList<javali_Identifier> javali_identifiers,        ArrayList<javali_Expression> javali_expressions    ) {
        this.javali_identifiers = javali_identifiers;
        this.javali_expressions = javali_expressions;
    }


    public List<javali_Identifier> getJavali_identifiers() {
        return javali_identifiers;
    }

    public void addJavali_identifier(Javali_identifier javali_identifier) {
        this.javali_identifiers.add(javali_identifier);
    }
    public List<javali_Expression> getJavali_expressions() {
        return javali_expressions;
    }

    public void addJavali_expression(Javali_expression javali_expression) {
        this.javali_expressions.add(javali_expression);
    }
    public javali_VarAssign getJavali_varassign() {
        return javali_varassign;
    }

    public void setJavali_varassign(javali_VarAssign javali_varassign) {
        this.javali_varassign = javali_varassign;
    }

}