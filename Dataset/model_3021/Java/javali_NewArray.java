





import java.util.List;
import java.util.ArrayList;

public class javali_NewArray extends Expression {






    private javali_Identifier javali_identifier;




    private List<javali_Expression> javali_expressions;


    public javali_NewArray(
    ) {
        super(
        );
        this.javali_expressions = new ArrayList<>();
    }

    public javali_NewArray(
        ArrayList<javali_Expression> javali_expressions    ) {
        this.javali_expressions = javali_expressions;
    }


    public javali_Identifier getJavali_identifier() {
        return javali_identifier;
    }

    public void setJavali_identifier(javali_Identifier javali_identifier) {
        this.javali_identifier = javali_identifier;
    }
    public List<javali_Expression> getJavali_expressions() {
        return javali_expressions;
    }

    public void addJavali_expression(Javali_expression javali_expression) {
        this.javali_expressions.add(javali_expression);
    }

}