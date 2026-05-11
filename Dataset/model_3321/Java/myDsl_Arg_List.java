





import java.util.List;
import java.util.ArrayList;

public class myDsl_Arg_List  {






    private myDsl_Expression_aux mydsl_expression_aux;




    private myDsl_Expression mydsl_expression;




    private List<myDsl_Expression> mydsl_expressions;


    public myDsl_Arg_List(
    ) {
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_Arg_List(
        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.mydsl_expressions = mydsl_expressions;
    }


    public myDsl_Expression_aux getMydsl_expression_aux() {
        return mydsl_expression_aux;
    }

    public void setMydsl_expression_aux(myDsl_Expression_aux mydsl_expression_aux) {
        this.mydsl_expression_aux = mydsl_expression_aux;
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