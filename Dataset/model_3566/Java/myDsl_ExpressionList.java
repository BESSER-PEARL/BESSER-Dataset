





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExpressionList  {






    private myDsl_Expression mydsl_expression;




    private List<myDsl_Expression> mydsl_expressions;


    public myDsl_ExpressionList(
    ) {
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_ExpressionList(
        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.mydsl_expressions = mydsl_expressions;
    }


    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public List<myDsl_Expression> getMydsl_expressions() {
        return mydsl_expressions;
    }

    public void addMydsl_expression(Mydsl_expression mydsl_expression) {
        this.mydsl_expressions.add(mydsl_expression);
    }

}