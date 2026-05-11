





import java.util.List;
import java.util.ArrayList;

public class myDsl_and_expressionR  {






    private myDsl_and_expression mydsl_and_expression;




    private List<myDsl_and_expressionR> mydsl_and_expressionrs;


    public myDsl_and_expressionR(
    ) {
        this.mydsl_and_expressionrs = new ArrayList<>();
    }

    public myDsl_and_expressionR(
        ArrayList<myDsl_and_expressionR> mydsl_and_expressionrs    ) {
        this.mydsl_and_expressionrs = mydsl_and_expressionrs;
    }


    public myDsl_and_expression getMydsl_and_expression() {
        return mydsl_and_expression;
    }

    public void setMydsl_and_expression(myDsl_and_expression mydsl_and_expression) {
        this.mydsl_and_expression = mydsl_and_expression;
    }
    public List<myDsl_and_expressionR> getMydsl_and_expressionrs() {
        return mydsl_and_expressionrs;
    }

    public void addMydsl_and_expressionr(Mydsl_and_expressionr mydsl_and_expressionr) {
        this.mydsl_and_expressionrs.add(mydsl_and_expressionr);
    }

}