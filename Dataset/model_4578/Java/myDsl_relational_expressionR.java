





import java.util.List;
import java.util.ArrayList;

public class myDsl_relational_expressionR  {






    private myDsl_shift_expression mydsl_shift_expression;




    private myDsl_relational_expression mydsl_relational_expression;




    private List<myDsl_relational_expressionR> mydsl_relational_expressionrs;


    public myDsl_relational_expressionR(
    ) {
        this.mydsl_relational_expressionrs = new ArrayList<>();
    }

    public myDsl_relational_expressionR(
        ArrayList<myDsl_relational_expressionR> mydsl_relational_expressionrs    ) {
        this.mydsl_relational_expressionrs = mydsl_relational_expressionrs;
    }


    public myDsl_shift_expression getMydsl_shift_expression() {
        return mydsl_shift_expression;
    }

    public void setMydsl_shift_expression(myDsl_shift_expression mydsl_shift_expression) {
        this.mydsl_shift_expression = mydsl_shift_expression;
    }
    public myDsl_relational_expression getMydsl_relational_expression() {
        return mydsl_relational_expression;
    }

    public void setMydsl_relational_expression(myDsl_relational_expression mydsl_relational_expression) {
        this.mydsl_relational_expression = mydsl_relational_expression;
    }
    public List<myDsl_relational_expressionR> getMydsl_relational_expressionrs() {
        return mydsl_relational_expressionrs;
    }

    public void addMydsl_relational_expressionr(Mydsl_relational_expressionr mydsl_relational_expressionr) {
        this.mydsl_relational_expressionrs.add(mydsl_relational_expressionr);
    }

}